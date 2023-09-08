# 🍜 Use Menu 

Camomilla provides a way to render menus.

To render a menu use the dedicated tags in your template:

```html
{% load menus %}
...
<header>
    {% render_menu "main_menu template_path="website/menu.html" %}
</header>
...
```

Camomilla will create a menu and render it.
The template_path kwarg is used to specify the html you want to use to render the menu.


