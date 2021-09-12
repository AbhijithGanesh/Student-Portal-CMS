python-3.9.7
web: python manage.py makemigrations && python manage.py migrate
python manage.py collectstatic
web: gunicorn StudentCMS.wsgi:app -w 4 -k uvicorn.workers.UvicornWorker 