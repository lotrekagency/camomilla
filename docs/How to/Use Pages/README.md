# 📝 Use Pages 

## The Page Model

Camomilla has it's own page model. The page model has an attribute for every relevant data in a web page. It takes care of SEO data and permalinks and template, and exposes jsonfields to manage additional data.

To use camomilla pages you need to add the dynamic url resolver at the end of your website urlpatterns:

```python
# <project_name>/urls.py
urlpatterns += path('', include("camomilla.dynamic_pages_urls"))
```
To handle multilanguage pages use:
```python
# <project_name>/urls.py
urlpatterns += i18n_patterns(
    path('', include("camomilla.dynamic_pages_urls")),
    prefix_default_language=False
)
```
This resolver is made to check any permalink that does not match anything in the url pattern and look in the database for a page with that permalink.

::: warning ⚠️ Beware!
The `dynamic_pages_urls` handler should always be the last handler of your urlpatterns list.
:::

### Choose the template

The page model has a field that determines which html template to use for rendering.
The default value is `defaults/pages/default.html`. If a value is stored in this field it will be used. The rendering part is yelded by the default [django template engine](https://docs.djangoproject.com/en/4.2/topics/templates/).
The default value can be changed with a setting:

```python
# <project_name>/settings.py
CAMOMILLA = {
    "RENDER": { "PAGE": {"DEFAULT_TEMPLATE": "website/my_template.html" }}
}
```

### Add template data

The data that will be available in the rendering engine should be saved in the template_data field. This field is a django JSONField. So it will accept any json structure.
The data in this field will be accessible inside the template through `page.template_data`.
If you need to enrich the template context with other data that are not stored in the template data you can provide an `inject_context` function in camomilla settings:

```python
# <project_name>/settings.py

# import from external file
from my_project_app.template_rendering import page_inject_context

# or define explicitly in settings
def page_inject_context(request, super_ctx):
    from my_project_app.models import Category
    return {"all_categories": Category.objects.all()} # the all_category values will be accessible inside the template context.


CAMOMILLA = {
    "RENDER": { "PAGE": {"INJECT_CONTEXT": page_inject_context }}
}
```

### Set the permalink

By default camomilla Page gives you the possibility to define the page `slug` field only.
The permalink will be generated from page `slug` and `parent_page` field.
With parent page field you can set a parent-child structure to pages.

For example to generate the permalink `slug1/slug2` you will need to create 2 Pages, one with slug `slug1` and one with the slug `slug2` then set the first page as the parent page of the second. 

## The AbstractPage Model 

Camomilla comes with an `AbstractPage` model. AbstractPage is different from Page model, it is Abstract.
This means that the AbstractPage by itself does not create a database table. The only whay an AbstractPage can have its own db table is to be inherited by a concrete model like this:


```python
from camomilla.models import AbstractPage

class MyPageModel(AbstractPage):
    # ... custom logic there
    pass

```


The AbstractPage contains all the logics of Page model. This means that you can override anything and define multiple custom page models. This is very usefull if you need to build complex sites, where you can have also other kid of data that need to be rendered and treated like a page (es. product, category, blog, anything..).


You can also define some intresting properties when you are defining your own page model.:

### Define page options with PageMeta


Many "settings" of the page model are stored inside a `PageMeta` class like this:

```python
from camomilla.models import AbstractPage

class MyPageModel(AbstractPage):
    class PageMeta:
        parent_page_field = "parent_page"
        default_template = "website/my_template.html"
        def inject_context_func(request, super_ctx):
            from my_project_app.models import Category
            return {"all_categories": Category.objects.all()}
```

From PageMeta class you can define: 

- `parent_page_field` ==> set a different propery to store page parent. Like `category` or anything else.
- `default_template` ==> set a different default template.
- `inject_context_func` ==> add more data inside template context

### Override the page context

This has almost the same functionality of `inject_context_func` PageMeta option but it runs at a more deep level. Overriding this will override the context and not only add things to it.


```python
from camomilla.models import AbstractPage

class MyPageModel(AbstractPage):
    def get_context(request):
        from my_project_app.models import Category
        return {"page": self, "all_categories": Category.objects.all()}
```

We suggest to always return `{ "page": self }` in the context. 