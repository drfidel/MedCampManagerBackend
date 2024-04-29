source venv/bin/activate

cd medcampsite_be

python manage.py makemigrations --settings=medcampsite_be.settings.local

python manage.py migrate --settings=medcampsite_be.settings.local


