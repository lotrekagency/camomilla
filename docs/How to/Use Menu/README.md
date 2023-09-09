# 🍜 Use Menu 

Camomilla comes with a menu system that allows you to create and render menus in your templates.

To render a menu you need only to load menu tags and use the `render_menu` tag.

```html
{% load menus %}
...
<header>
    {% render_menu "main_menu" %}
</header>
...
```
The `render_menu` tag will create or fetch from the database a menu with the name specified in the first argument and render it using the default template.

If you want to use a custom template you can specify the path to the template in the second argument.

```html
{% load menus %}
...
<header>
    {% render_menu "main_menu" "website/parts/menu.html" %}
</header>
...
```

### The Default Template
If no template_path is specified, the default template will be used.

The default template is very simple and looks like this: 


```html
<!-- Take inspiration from this template to create your own! -->

{% load menus %}
{% if menu.nodes|length %}
<ul>
  {% for item in menu.nodes %}
  <li>
    {% if item.link.url %}
      <a href="{{ item.link.url }}">{{ item.title }}</a>
    {% else %}
      <span>{{item.title}}</span>
    {% endif %}
    {% include 'defaults/parts/menu.html' with menu=item %} 
  </li>
  {% endfor %}
</ul>
{% endif %}
```




