import multiprocessing
import os

bind = "{0}:{1}".format(os.environ.get('HOST', '127.0.0.1'), os.environ.get('PORT', '8080'))
workers = os.environ.get('WORKERS', multiprocessing.cpu_count() * 2 + 1)
