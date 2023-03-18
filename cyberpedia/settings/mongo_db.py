DATABASES = {
    'default': {
        'ENGINE':'djongo',
        'NAME': 'cyberpedia',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            "host": "localhost:27017"
        }
    },

}