web: gunicorn airport_transfer.wsgi
worker: celery -A airport_transfer worker --loglevel=info
heroku config:set DISABLE_COLLECTSTATIC=1