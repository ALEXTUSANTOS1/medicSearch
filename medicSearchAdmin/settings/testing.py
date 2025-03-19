import os
from .settings import *

DEBUG  =  False

'Senha para o ambiente de produção'
SECRET_KEY = 'A13xTu!10$12'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' : os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}