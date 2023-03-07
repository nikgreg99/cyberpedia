import requests


class UrlHaus():
    base_url : str = "https://urlhaus-api.abuse.ch/v1/urls"
    api_key = None
    urlhaus = requests.Session()