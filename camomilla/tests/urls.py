from django.urls import include, path



def dummy_view(request):
    from django.http import HttpResponse
    return HttpResponse("Here's the text of the Web page.")

urlpatterns = [
    path('articles/<slug:title>', dummy_view, name='article-detail'),
]

