# Deploy Camomilla core

## Installation

Follow the README.md to setup a complete virtual environment on your server

## Server with Gunicorn + Apache

Camomilla core can be deployed behind an Apache server with reverse proxy enabled. First of all you need to install Gunicorn with

    $ pip install gunicorn

Create your Gunicorn.py file and configure it, starting from gunicorn_settings_example.py, then launch Gunicorn in your server

    $ gunicorn camomillabench.wsgi -c gunicorn_settings.py

If you want to keep your core behind a prefix, in your local_settings.py add

    ULR_PREFIX = 'yourprefix'

Remember to configure Apache with a reverse proxy and let Apache serving your static and media files and reverse proxing your core.

    <Directory />
        Options FollowSymLinks
        AllowOverride None
        Require all denied
    </Directory>

    <Directory /usr/share>
        AllowOverride None
        Require all granted
    </Directory>

    # PHP directives and .htaccess

    <Directory /var/www/>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>

    <Directory /var/www/html>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride all
        Order allow,deny
        allow from all
    </Directory>

    # Reverse Proxy

    <Proxy http://127.0.0.1:8080/*>
        Allow from all
    </Proxy>

    <LocationMatch "/panel">
        ProxyPass http://127.0.0.1:8080/panel
        ProxyPassReverse http://127.0.0.1:8080/panel
    </LocationMatch>

    <Location /static>
        ProxyPass "!"
    </Location>

    # Serve media and static files

    Alias /media/  /root/core/media/
    Alias /static/  /root/core/static/

    <Directory /root/core/media>
        Require all granted
    </Directory>

    <Directory root/core//static>
        Require all granted
    </Directory>
