# Camomilla 4.0

## Install

	$ pip install -r requirements.txt

In you encounter some problems during mysqlclient installation

    $ env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install mysqlclient

## Setup database

Create camomilla/local_settings.py file and write your database configuration, based on local_settings_example.py:

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

## Run the server

    $ python manage.py runserver

## References

- http://www.django-rest-framework.org/
- https://github.com/DjangoBeer/drf-tutorial
