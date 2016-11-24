import multiprocessing
import os

if not 'HOST' in os.environ and not 'PORT' in 'HOST':
    bind = "unix:{0}".format(os.environ.get('SOCKET', 'gunicorn.socket'))
else:
    bind = "{0}:{1}".format(os.environ.get('HOST', '127.0.0.1'), os.environ.get('PORT', '8080'))
workers = os.environ.get('WORKERS', multiprocessing.cpu_count() * 2 + 1)
