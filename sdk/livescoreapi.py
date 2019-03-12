import urllib.request
import requests
import re
import datetime
from urllib.parse import urlparse


class LivescoresAPI: 

    language_list = ['ar', 'ru', 'fa']
    api_url = ''
    api_key = ''
    api_secret = ''
    language = ''

    def __init__(self, api_url, api_key, api_secret, language):
        self.validate_url(api_url)
        self.validate_key(api_key)
        self.validate_secret(api_secret)
        if language is not None:
            self.validate_language(language)

        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.language = language


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
        url = '{}scores/live.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)

        if country_id is not None:
            self.validate_country(country_id)
            url = url + '&country=' + str(country_id)

        if self.language is not None:
            url = url + '&lang=' + self.language

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


    def validate_date(self, date):

        if date is None:
            raise ValueError('Date must be defined')

        if not (isinstance(date, str)):
            raise ValueError("Date must be a string")

        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be %Y-%m-%d")

    def validate_page(self, page):
        
        if page is None:
             raise ValueError('Page ID must be defined')

        if not (isinstance(page, int)):
            raise ValueError("Page ID must be a integer")

        if page < 1:
            raise ValueError("Page ID must be a positive number")


    def get_all_fixtures(self, league_id, date, page):
        url = '{}fixtures/matches.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)

        if league_id is not None:
            self.validate_league(league_id)
            url = url + '&league=' + str(league_id)

        if date is not None:
            self.validate_date(date)
            url = url + '&date=' + str(date)

        if self.language is not None:
            url = url + '&lang=' + self.language

        if page is not None:
            self.validate_page(page)
            url = url + '&page=' + str(page)

        fixtures = requests.get(url)
        return fixtures.json()['data']['fixtures']


    def get_fixtrures_by_league(self, league_id, page):
        return self.get_all_fixtures(league_id, None, page)


    def get_today_fixtures(self, page):
        today = str(datetime.datetime.today())[:10]
        return self.get_all_fixtures(None, today, page)


    def get_tomorrow_fixtures(self, page):
        tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))[:10]
        return self.get_all_fixtures(None, tomorrow, page)


    def get_history_matches(self, from_date, to_date, league_id, page, language):
        url = '{}scores/history.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)

        if from_date is not None:
            self.validate_date(from_date)
            url = url + '&from=' + str(from_date)

        if to_date is not None:
            self.validate_date(to_date)
            url = url + '&to=' + str(to_date)
        
        if league_id is not None:
            self.validate_league(league_id)
            url = url + '&league=' + str(league_id)

        if page is not None:
            self.validate_page(page)
            url = url + '&page=' + str(page)

        if self.language is not None:
            url = url + '&lang=' + self.language


        history_fixtures = requests.get(url)
        return history_fixtures.json()['data']['match']


    def get_history_matches_by_league(self, league_id, page, language):
        return self.get_history_matches(None, None, league_id, page, language)


    def get_history_matches_by_league_and_from_date(self, from_date, league_id, page, language):
        return self.get_history_matches(from_date, None, league_id, page, language)


    def get_history_matches_by_league_and_to_date(self, to_date, league_id, page, language):
        return self.get_history_matches(None, to_date, league_id, page, language)


    def get_history_matches_from_date(self, from_date, page, language):
        return self.get_history_matches(from_date, None, None, page, language)

    
    def get_history_matches_to_date(self, to_date, page, language):
        return self.get_history_matches(None, to_date, None, page, language)

    
    def get_history_matches_from_date_to_date(self, from_date, to_date, page, language):
        return self.get_history_matches(from_date, to_date, None, page, language)


    def get_history_matches_for_yesterday(self, page, language):
        yesterday = str(datetime.date.today() - datetime.timedelta(days=1))[:10]
        return self.get_history_matches(yesterday, None, None, page, language)


    def get_history_matches_for_last_week(self, page, language):
        last_week = str(datetime.date.today() - datetime.timedelta(days=7))[:10]
        return self.get_history_matches(last_week, None, None, page, language)


    def get_history_matches_for_last_weekend(self, from_date, to_date, page, language): 
        fri = str(datetime.date.today() - datetime.timedelta(7+((datetime.date.today().weekday() + 1) % 7)-5))
        sun = str(datetime.date.today() - datetime.timedelta(7+((datetime.date.today().weekday() + 1) % 7)-7))
        return self.get_history_matches(fri, sun, None, page, language)

    
    def get_history_matches_for_last_month(self, page, language):
        last_month = str(datetime.date.today() - datetime.timedelta(days=30))[:10]
        return self.get_history_matches(last_month, None, None, page, language)

    
    def get_history_matches_for_last_year(self, page, language):
        last_year= str(datetime.date.today() - datetime.timedelta(days=365))[:10]
        return self.get_history_matches(last_year, None, None, page, language)


    def get_all_countries(self):
        url = '{}countries/list.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)
        list_of_countries = requests.get(url)
        return list_of_countries.json()['data']['country']


    def get_all_leagues(self):
        url = '{}leagues/list.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)
        list_of_leagues = requests.get(url)
        return list_of_leagues.json()['data']['league']
    

    def get_all_leagues_with_fixtures(self):
        url = '{}fixtures/leagues.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)
        list_of_leagues_with_fixtures = requests.get(url)
        return list_of_leagues_with_fixtures.json()['data']['leagues']


   