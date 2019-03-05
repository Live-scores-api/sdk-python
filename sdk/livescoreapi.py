import urllib.request
import requests
import re
import datetime
from urllib.parse import urlparse


class Livescores: 

    @staticmethod
    def validate_key(api_key):
        if api_key is None:
            raise ValueError("Api key cannot be None")

        if type(api_key) != str:
            raise ValueError("Api key must be a string")

        if not(re.match("^[A-Za-z0-9]*$", api_key)) or len(api_key) != 16:
            raise ValueError("Api key has invalid format")

        return
    
    @staticmethod
    def validate_secret(api_secret):
        if not api_secret:
            raise ValueError("None API Secret!")
        if re.match("^[A-Za-z0-9]*$", api_secret) and len(api_secret) == 32:
            return True
        else:
            raise ValueError("Wrong API Secret!")

    def validate_url(self, api_url):
        if not api_url:
            raise ValueError("None API URL!")

    language_list = ['en', 'ar', 'ru', 'fa']
    api_url = 'http://livescore-api.com/api-client/'
    api_key = '5555YYYYgggg21aD'
    api_secret = '5555YYYYgggg21aDKKKK2222ssssYYYY'

    def __init__(self, api_url, api_key, api_secret, language='en'):
        self.validate_url(api_url)
        self.validate_key(api_key)
        self.api_secret = api_secret

        if api_secret is not None:
            self.validate_secret(api_secret)

        self.api_url = api_url
        self.api_key = api_key
        lang_check = self.validate_language(language)
        if lang_check is True:
            self.lang = language

    def get_all_livescores(self, country_id, league_id):
        url = '{}scores/live.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)
        if country_id is not None:
            self.validate_country(country_id)
            url = url + '&country=' + str(country_id)
        #if language_id is not None:
        #    self.validate_language(language_id)
         #   url = url + '&lang=' + language_id
        if league_id is not None:
            self.validate_league(league_id)
            url = url + '&league=' + str(league_id)
        livescores = requests.get(url)
        return livescores.json()


    def validate_country(self, country_id):
        if country_id is None:
            raise ValueError("Country ID must be defined")
        if not (isinstance(country_id, int)):
            raise ValueError("Country ID must be a integer")
        if country_id <= 0:
            raise ValueError("Country ID must be a positive number")
        
       
    def validate_language(self, language_id): 
        if language_id is None:
             raise ValueError("Language ID must be defined")
        if not (isinstance(language_id, str)):
            raise ValueError("Language ID must be a string")
        if language_id in self.language_list:
            return True


    def validate_league(self, league_id):
        if league_id is None:
            raise ValueError("League ID must be defined")
        if not (isinstance(league_id, int)):
            raise ValueError("League ID must be a integer")
        if league_id <= 0:
            raise ValueError("Wrong league ID")


    def get_livescores_by_country(self, country_id):
        return self.get_all_livescores(country_id, None)

                
    def get_livescores_by_league(self, league_id):
        return self.get_all_livescores(None, league_id)


    def get_all_fixtrures(self, country_id, league_id, date):
        url = '{}fixtures/matches.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)
        if country_id is not None:
            self.validate_country(country_id)
            url = url + '&country_id=' + str(country_id)
        if league_id is not None:
            self.validate_league(league_id)
            url = url + '&league=' + str(league_id)
        #if language_id is not None:
         #   self.validate_language(language_id)
          #  url = url + '&lang=' + language_id
        fixtures = requests.get(url)
        return fixtures.json()


    def get_fixtrures_by_country(self, country_id):
        return self.get_all_fixtrures(country_id, None, None)


    def get_todays_fixtures(self):
        return self.get_all_fixtrures(None, None, date)