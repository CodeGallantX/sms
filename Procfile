web: gunicorn school_management.wsgi:application --log-file -
worker: celery -A school_management worker -l info
beat: celery -A school_management beat -l info
daphne: daphne -p $PORT school_management.asgi:application
