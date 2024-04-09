# BlogsDjango

This project used class base view, form and model forms.

# To setup 

## Create virtualenv


    python -m venv virtualenv

    .\virtualenv\Scripts\activate

    pip freeze -r .\requirements.txt


## Setup db in MySQL


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db_dev_blogs_django',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }


Run Migration commands

    python manage.py migrate


## Create superuser

    python manage.py createsuperuser




    