import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from camomilla.models import Tag, Category

client = APIClient()


def login_superuser():
    User.objects.create_superuser("admin", "myemail@test.com", "adminadmin")
    response = client.post(
        "/api/camomilla/token-auth/", {"username": "admin", "password": "adminadmin"}
    )
    return response.json()["token"]


@pytest.mark.django_db
def test_create_tag_no_access():
    response = client.post("/api/camomilla/tags/", {"title": "First tag"})
    assert response.json()["detail"] == "Authentication credentials were not provided."
    assert response.status_code == 403


@pytest.mark.django_db
def test_crud_tag():
    ## Create
    token = login_superuser()
    client.credentials(HTTP_AUTHORIZATION="Token " + token)
    response = client.post("/api/camomilla/tags/", {"title": "Primo tag"})
    assert response.json()["title"] == "Primo tag"
    assert response.json()["language_code"] == "it"

    assert len(Tag.objects.all()) == 1
    assert response.status_code == 201

    ## Create another with a different language
    response = client.post(
        "/api/camomilla/tags/", {"title": "Second tag", "language_code": "en"}
    )
    assert response.json()["title"] == "Second tag"
    assert response.json()["language_code"] == "en"

    assert len(Tag.objects.all()) == 2

    assert response.status_code == 201

    ## Translate the second one in italian
    response = client.patch(
        "/api/camomilla/tags/2/", {"title": "Secondo tag", "language_code": "it"}
    )
    assert response.json()["title"] == "Secondo tag"
    assert response.json()["language_code"] == "it"

    assert len(Tag.objects.all()) == 2

    assert response.status_code == 200

    ## Get the tags in 🇮🇹
    response = client.get("/api/camomilla/tags/")

    assert response.json()[0]["title"] == "Secondo tag"
    assert response.json()[0]["language_code"] == "it"

    ## Get the tags in 🇬🇧 with fallbacks!
    response = client.get("/api/camomilla/tags/?language=en")

    assert response.json()[0]["title"] == "Second tag"
    assert response.json()[0]["language_code"] == "en"

    ## Delete the tag
    response = client.delete("/api/camomilla/tags/2/")

    assert len(Tag.objects.all()) == 1

    assert response.status_code == 204
