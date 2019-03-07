import urllib.request
import requests
import re
import datetime
from urllib.parse import urlparse


class LivescoresAPI: 

    language_list = ['en', 'ar', 'ru', 'fa']
    api_url = ''
    api_key = ''
    api_secret = ''
    

    def __init__(self, api_url, api_key, api_secret, language):
        self.validate_url(api_url)
        self.validate_key(api_key)
        self.validate_secret(api_secret)
        self.validate_language(language)

        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.lang = language


    @staticmethod
    def validate_key(api_key):

        if api_key is None:
            raise ValueError("API Key must be defined!")

        if not (isinstance(api_key, str)):
            raise ValueError("API Key must be a string")
        
        if not(re.match("^[A-Za-z0-9]*$", api_key)) or len(api_key) != 16:
            raise ValueError("Invalid API Key format!")
        

    @staticmethod
    def validate_secret(api_secret):

        if api_secret is None:
            raise ValueError("API Secret must be defined!")

        if not (isinstance(api_secret, str)):
            raise ValueError("API Secret must be a string") 

        if not(re.match("^[A-Za-z0-9]*$", api_secret)) or len(api_secret) != 32:
            raise ValueError("Invalid API Secret format!") 


    @staticmethod
    def validate_url(api_url):

        if api_url is None:
            raise ValueError("API URL must be defined!")

        if not (isinstance(api_url, str)):
            raise ValueError("API URL must be a string")

        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if not re.match(regex, api_url):
            raise ValueError("API URL is not valid")

        if "livescore-api.com" not in api_url:
            raise ValueError("API URL does not contain livescore-api.com")
    
    def get_all_livescores(self, country_id, league_id):
        url = '{}scores/live.json?key={}&secret={}&lang={}'.format(self.api_url, self.api_key, self.api_secret, self.lang)

        if country_id is not None:
            self.validate_country(country_id)
            url = url + '&country=' + str(country_id)

        if league_id is not None:
            self.validate_league(league_id)
            url = url + '&league=' + str(league_id)

        livescores = requests.get(url)
        return livescores.json()['data']['match']


    def validate_country(self, country_id):

        if country_id is None:
            raise ValueError("Country ID must be defined")
            
        if not (isinstance(country_id, int)):
            raise ValueError("Country ID must be an integer")

        if country_id < 1:
            raise ValueError("Country ID must be a positive number")
        
       
    def validate_language(self, language_id): 

        if language_id is None:
            raise ValueError("Language ID must be defined")

        if not (isinstance(language_id, str)):
            raise ValueError("Language ID must be a string")

        if language_id not in self.language_list:
            raise ValueError("Language ID is not supported")


    def validate_league(self, league_id):

        if league_id is None:
            raise ValueError("League ID must be defined")

        if not (isinstance(league_id, int)):
            raise ValueError("League ID must be a integer")

        if league_id < 1:
            raise ValueError("League ID must be a positive number")


    def get_livescores_by_country(self, country_id):
        return self.get_all_livescores(country_id, None)

                
    def get_livescores_by_league(self, league_id):
        return self.get_all_livescores(None, league_id)


   