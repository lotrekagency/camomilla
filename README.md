# Camomilla 4.0 (pre-alpha)

## Install

	$ pip install -r requirements.txt

If you encounter some problems during mysqlclient installation on Mac, please reinstall it using:

    $ env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install mysqlclient

If you encounter some problems during mysqlclient installation on Windows, follow the instructions displayed on your console, you need the Visual C++ compiler installed.

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

After that you can launch all the migrations

    $ python manage.py migrate

And create a super user to start managing your project

    $ python manage.py createsuperuser

## Run the server

    $ python manage.py runserver

## A note for pre alpha adopters

In case you want to test and/or use Camomilla 4.0 pre-alpha: we don't want to track a lot of migrations, so we throw away all the migrations before the official release. If you want update Camomilla please delete and create your database again, then launch all the migrations with

    $ python manage.py migrate

You need to create your user again as well

## References for developers

- http://www.django-rest-framework.org/
- https://github.com/FuzzyBrains/drf-intro/
- https://github.com/DjangoBeer/drf-tutorial/
