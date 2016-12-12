#!/bin/bash

# Get configuration
source deploy_settings.sh

# Check configuration

if [ -z "$PROJECT_NAME" ]; then
    echo "Please set PROJECT_NAME variable!"
    exit 1
fi

if [ ! -f $PROJECT_NAME/local_settings.py ]; then
    echo "Please define $PROJECT_NAME/local_settings.py!"
    exit 1
fi

# Kill the old process
pkill gunicorn_$PROJECT_NAME

# Prepare the code
if [ "$1" = "reset" ]; then
    git stash
    git checkout master
    git fetch origin
    git merge origin/master
fi

# Prepare virtualenv
rm -rf venv
virtualenv venv -p $PYTHON_PATH
. venv/bin/activate
pip install -r requirements.txt

pip install gunicorn
pip install setproctitle

# Prepare FE libraries
npm install

# Compile static
grunt build
python manage.py collectstatic -l --no-input

# Migrate the database
python manage.py migrate

# Create MUST HAVE deploy settings
echo "DEBUG=False" > $PROJECT_NAME/deploy_settings.py
echo "ALLOWED_HOSTS = ['*']" >> $PROJECT_NAME/deploy_settings.py
echo "ADMIN_URL='admin_$PROJECT_NAME_$ADMIN_URL_SUFFIX'" >> $PROJECT_NAME/deploy_settings.py

# Run gunicorn
gunicorn $PROJECT_NAME.wsgi -c gunicorn_settings.py --name gunicorn_$PROJECT_NAME --log-file error_logs.log --capture-output &
