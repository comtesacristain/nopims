from django.conf import settings
settings.configure(
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/Users/michael/Public/nopims/nopta.db',
        }
    }
)