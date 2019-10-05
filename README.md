# Camomilla 5.0 alpha

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

