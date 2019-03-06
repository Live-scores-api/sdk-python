import urllib.request
import requests
import re
import datetime
from urllib.parse import urlparse


class LivescoresAPI: 

    language_list = ['en', 'ar', 'ru', 'fa']
    api_url = 'http://livescore-api.com/api-client/'
    api_key = ''
    api_secret = ''


    def __init__(self, api_url, api_key, api_secret, language='en'):
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
        if not (isinstance(api_key, str)):
            raise ValueError("API Key must be a string")
        if not api_key:
            raise ValueError("API Key cannot be None!")
        if not(re.match("^[A-Za-z0-9]*$", api_key)) or len(api_key) != 16:
            raise ValueError("Invalid API Key format!")
        

    @staticmethod
    def validate_secret(api_secret):
        if not (isinstance(api_secret, str)):
            raise ValueError("API Secret must be a string") 
        if not api_secret:
            raise ValueError("API Secret cannot be None!")
        if not(re.match("^[A-Za-z0-9]*$", api_secret)) or len(api_secret) != 32:
            raise ValueError("Invalid API Secret format!") 


    @staticmethod
    def validate_url(api_url):
        if not (isinstance(api_url, str)):
            raise ValueError("API URL must be a string")
        if not api_url:
            raise ValueError("API URL cannot be None!")
    
    
    def get_all_livescores(self, country_id, league_id):
        url = '{}scores/live.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)
        if country_id is not None:
            self.validate_country(country_id)
            url = url + '&country=' + str(country_id)
        if league_id is not None:
            self.validate_league(league_id)
            url = url + '&league=' + str(league_id)
        livescores = requests.get(url)
        return livescores.json()


    def validate_country(self, country_id):
        if not country_id:
            raise ValueError("Country ID must be defined")
        if not (isinstance(country_id, int)):
            raise ValueError("Country ID must be a integer")
        if country_id <= 0:
            raise ValueError("Country ID must be a positive number")
        
       
    def validate_language(self, language_id): 
        if not language_id:
             raise ValueError("Language ID must be defined")
        if not (isinstance(language_id, str)):
            raise ValueError("Language ID must be a string")
        if language_id in self.language_list:
            return True


    def validate_league(self, league_id):
        if not league_id:
            raise ValueError("League ID must be defined")
        if not (isinstance(league_id, int)):
            raise ValueError("League ID must be a integer")
        if league_id <= 0:
            raise ValueError("League ID must be a positive number")


    def validate_date(self, date):
        if not date:
            raise ValueError('Date must be defined')
        

    def get_livescores_by_country(self, country_id):
        return self.get_all_livescores(country_id, None)

                
    def get_livescores_by_league(self, league_id):
        return self.get_all_livescores(None, league_id)


    def get_all_fixtures(self, country_id, league_id, date):
        url = '{}fixtures/matches.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)
        if country_id is not None:
            self.validate_country(country_id)
            url = url + '&country_id=' + str(country_id)
        if league_id is not None:
            self.validate_league(league_id)
            url = url + '&league=' + str(league_id)
        if date is not None:
            self.validate_date(date)
            url = url + '&date=' + str(date)
        fixtures = requests.get(url)
        return fixtures.json()


    def get_fixtures_by_country(self, country_id):
        return self.get_all_fixtures(country_id, None, None)


    def get_fixtrures_by_league(self, league_id):
        return self.get_all_fixtures(None, league_id, None)


    def get_today_fixtures(self):
        today = str(datetime.datetime.today())[:10]
        return self.get_all_fixtures(None, None, today)


    def get_tomorrow_fixtures(self):
        tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))[:10]
        return self.get_all_fixtures(None, None, tomorrow)