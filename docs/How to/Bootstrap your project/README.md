# 🚀 Bootstrap your project


## 📦 Quick Setup

### Install 


```bash
$ pip install django-camomilla-cms==6.0.0b1
```

## 🔨 Settings


Camomilla brings a lot of default settings you can include in your project's ones

```python
from camomilla.defaults import *
```

Remember to add all the required applications in your project


```python
INSTALLED_APPS = [
    ...
    'camomilla', # always needed
    'camomilla.theme', # needed to customize admin interface
    'djsuperadmin', # needed if you whant to use djsuperadmin for contents
    'modeltranslation', # needed if your website is multilanguage (can be added later)
    'rest_framework',  # always needed
    'rest_framework.authtoken',  # always needed
    ...
]
```

### Setup 


```bash
$ mkdir -p camomilla_migrations
$ touch camomilla_migrations.__init__.py
$ python manage.py makemigrations camomilla
$ python manage.py migrate camomilla
```

### Run the server

```bash
$ python manage.py runserver
```
