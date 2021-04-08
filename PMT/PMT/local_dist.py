import os
​
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'TotallyRealSecretKey'
​
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
​
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
​
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
​
​
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}