import urllib.request
import requests


class Livescores:

    api_url = 'http://livescore-api.com/api-client/'
    api_key = ''
    api_secret = ''


    def __init__(self, api_url, api_key, api_secret, lang="en"):
        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret

    
    def get_all_livescores(self, country_id, language_id, league_id):
        url = '{}scores/live.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)
        print(url)
        if country_id is not None:
            self.validate_country(country_id)
            url = url + '&country=' + str(country_id)
            print(url)
        if language_id is not None:
            self.validate_language(language_id)
            url = url + '&lang=' + language_id
            print(url)
        if league_id is not None:
            self.validate_league(league_id)
            url = url + '&league=' + str(league_id)
            print(url)
        livescores = requests.get(url)
        return livescores.json()


    def validate_country(self, country_id):
        if country_id is None:
            raise ValueError("Country ID must be defined")
        if not (isinstance(country_id, int)):
            raise ValueError("Country ID must be a integer")
        if country_id <= 0:
            raise ValueError("Wrong country ID")
        else: 
            return True
       
    def validate_language(self, language_id):
        language_list = ['en', 'ar', 'ru', 'fa']
        if language_id is None:
             raise ValueError("Language ID must be defined")
        if not (isinstance(language_id, str)):
            raise ValueError("Language ID must be a string")
        if language_id in language_list:
            return True


    def validate_league(self, league_id):
        if league_id is None:
            raise ValueError("League ID must be defined")
        if not (isinstance(league_id, int)):
            raise ValueError("League ID must be a integer")
        if league_id <= 0:
            raise ValueError("Wrong league ID")
        else: 
            return True


    def get_livescores_by_country(self, country_id, language_id):
        return self.get_all_livescores(country_id, language_id, None)

                
    def get_livescores_by_league(self, league_id, language_id):
        return self.get_all_livescores(None, language_id, league_id)

    def get_fixtrures(self, country_id, league_id, language_id, date):
        if country_id is not None:
            self.validate_country(country_id)
            url = url + '&country_id=' + country_id

        return []

    def get_fixtrures_by_country(self, country_id, language_id):
        return self.get_fixtrures(country_id, None, language_id, None)

    def get_todays_fixtures(self):
        return self.get_fixtrures(None, None, None, today())