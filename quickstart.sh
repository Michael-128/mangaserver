py manage.py makemigrations &&
py manage.py migrate &&
py manage.py collectstatic --no-input &&
py manage.py runserver 0.0.0.0:80
