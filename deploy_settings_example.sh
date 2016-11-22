# Deploy settings
PROJECT_NAME='camomillabench'
PYTHON_PATH='/usr/local/bin/python3.5'
ADMIN_URL_SUFFIX='van_halen_1984'

# Gunicorn settings
export WORKERS=6
export HOST='0.0.0.0'
export PORT=8090

# Here you can export variables and do other things if needed
# e.g.
# export LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib"
