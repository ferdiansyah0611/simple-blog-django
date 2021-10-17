echo "Reset"
rm db.sqlite3
python manage.py makemigrations
python manage.py makemigrations blog
python manage.py migrate
python manage.py createsuperuser