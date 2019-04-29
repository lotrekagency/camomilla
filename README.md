# Camomilla 4.0.1b

## Install

	$ pip install -r requirements.txt

If you encounter some problems during mysqlclient installation on Mac, please reinstall it using:

    $ env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install mysqlclient

If you encounter some problems during mysqlclient installation on Windows, follow the instructions displayed on your console, you need the Visual C++ compiler installed.

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

At the end of your settings file remember to include local_settings and deploy_settings


    try:
        from .deploy_settings import *
    except ImportError:
        pass

    try:
        from .local_settings import *
    except ImportError:
        print ("\n\nWARNING: No local_settings.py found! Please look at the README.md file!\n\n")


## Setup database

Create your_project/local_settings.py file and write your database configuration, based on local_settings_example.py:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'camomilla4',
            'USER': 'root',
            'PASSWORD': 'admin',
            'HOST': 'localhost',
        }
    }

After that, you can launch all the migrations

    $ python manage.py migrate

And create a super user to start managing your project

    $ python manage.py createsuperuser


## Extend the user

If you plan to customize the user, it's a good practice to extend the user before starting the project, In your app do something like this:

    from camomilla.models import CamomillaBaseUser


    class MyCustomProfile(CamomillaBaseUser):
        pass


And remember to put this in your local settings:

    AUTH_USER_MODEL = "plugin_profileslist.MyCustomProfile"

In case you want to provide a custom user in the middle of the project, consider one of these possible actions:

    - Delete the entire database
    - Make a [difficult migration](https://code.djangoproject.com/ticket/25313)
    - Create a 1 to 1 Profile relation with CamomillaUser

More about user customization [here](https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#substituting-a-custom-user-model)

## Run the server

    $ python manage.py runserver

## Run tests

Put Camomilla in a real Django project, then run

    $ coverage run --source='camomilla' manage.py test camomilla.tests

To see the coverage use

    $ coverage report

## Deploy on a real server

Please, read DEPLOY.md

## A note for pre alpha adopters

In case you want to test and/or use Camomilla 4.0 pre-alpha: we don't want to track a lot of migrations, so we throw away all the migrations before the official release. If you want update Camomilla please delete and create your database again, then launch all the migrations with

    $ python manage.py migrate

You need to create your user again as well

## Don't fear the hvader

Feel free to make your models untranslatable, [we have a nice solution for them](https://github.com/KristianOellegaard/django-hvad/issues/277)

## References for developers

- http://www.django-rest-framework.org/
- https://github.com/FuzzyBrains/drf-intro/
- https://github.com/DjangoBeer/drf-tutorial/
