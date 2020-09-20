from .base import *  # NOQA
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 3306,
        # 'OPTIONS': {'charset': 'utf8mb4'}
    }
}
