# 🐝 Use API 

Camomilla comes with many api endpoint builded with Django Rest Framework. 

To use the endpoints you need to add the handler to the project urls.py

```python
# <project_name>/urls.py
urlpatterns += path('api/camomilla/', include('camomilla.urls'))
```

::: warning ⚠️ Beware!
Remember that if you use camomilla pages `dynamic_pages_urls` handler should always be the last handler of your urlpatterns list.
:::


By default every endpoint comes with a full CRUD in the style of django rest framework with some mode feature beaked in.


## Get all items

__URL:__
 - `api/camomilla/articles`


__Response:__
```json
{
    "items": [
        ...
    ],
    "paginator": {
        "count": 1,
        "page": 1,
        "has_next": false,
        "has_previous": false,
        "pages": 1,
        "page_size": 10
    }
}
```