python-3.9.7
python manage.py makemigrations && python manage.py migrate
web: gunicorn StudentCMS.wsgi:app -w 4 -k uvicorn.workers.UvicornWorker 