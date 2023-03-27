## POKEMON API

#### Aim of the exercise

The goal of this project is to build an interactive Pokedex.


#### Tech/framework used

Project is created with:

* [Django](https://www.djangoproject.com/) version 4.1.7
* [Django REST framework](https://www.django-rest-framework.org/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [Django cors headers](https://pypi.org/project/django-cors-headers/)
* [Sqlite3](https://sqlite.org/index.html)
* [Pandas](https://pandas.pydata.org/)
* [Python](https://www.python.org/)

### Project setup

First install the project dependencies :
```
pip install -r requirements.txt
```

### Create database sqlite :
```
python manage.py makemigrations Pokemon
python manage.py migrate Pokemon
```

### To Register Pokemon data to sqlite
```
python manage.py runscript upload_csv
```

### Compiles and hot-reloads for development
```
python manage.py runserver
```

## Credits
- Koku Ulrich GBLOKPO @koku-ulrich.gblokpo


