# camomilla cms [![PyPI](https://img.shields.io/pypi/v/django-camomilla-cms?style=flat-square)](https://pypi.org/project/django-camomilla-cms) ![Codecov](https://img.shields.io/codecov/c/github/lotrekagency/camomilla?style=flat-square) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/lotrekagency/camomilla/Test,%20Coverage%20and%20Release?style=flat-square) [![GitHub](https://img.shields.io/github/license/lotrekagency/camomilla?style=flat-square)](./LICENSE)

## Install

	$ pip install -r requirements.txt

## Settings

Camomilla brings a lot of default settings you can include in your project's ones

    from camomilla.defaults import *

Remember to add all the required applications in your project

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'rest_framework.authtoken',
        'camomilla',
        'hvad',
        ...
    ]

## Run the server

    $ python manage.py runserver

## Run tests

    pip install -r requirements-dev.txt
    make test

## Don't fear the hvader

Feel free to make your models untranslatable, [we have a nice solution for them](https://github.com/lotrekagency/hvad-migration)

