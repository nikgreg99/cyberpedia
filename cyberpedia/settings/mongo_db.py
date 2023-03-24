DATABASES = {
    'default': {
        'ENGINE':'djongo',
        'NAME': 'cyberpedia',
        'ENFORCE_SCHEMA': True,
        'CLIENT': {
            "host": "localhost:27017"
        }
    }
}