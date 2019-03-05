import urllib.request
import requests
import re


def validate_key(api_key):
        if api_key is None:
            raise ValueError("Missing API Key!")
        if re.match("^[A-Za-z0-9_-]*$", api_key) and len(api_key) == 16:
            print("API key is according to requirements")
        else:
            raise ValueError("Wrong API Key!")
    

def validate_secret(api_secret):
    if api_secret is None:
        raise ValueError("Missing API Secret!")
    if re.match("^[A-Za-z0-9_-]*$", api_secret) and len(api_secret) == 32:
        print("API secret is according to requirements")
    else:
        raise ValueError("Wrong API Secret!")


class Livescores: 
    
    
    language_list = ['en', 'ar', 'ru', 'fa']
    api_url = 'http://livescore-api.com/api-client/'
    #print(urllib.request.urlopen(api_url).getcode())
    api_key = '5555YYYYgggg21aD'
    if api_key is not None:
        validate_key(api_key)
    api_secret = '5555YYYYgggg21aDKKKK2222ssssYYYY'
    if api_secret is not None:
        validate_secret(api_secret)
      

    def __init__(self, api_url, api_key, api_secret, lang):
        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret
        lang_check = self.validate_language(lang)
        if lang_check is True:
            self.lang = lang


    
    def get_all_livescores(self, country_id, language_id, league_id):
        url = '{}scores/live.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)
        if country_id is not None:
            self.validate_country(country_id)
            url = url + '&country=' + str(country_id)
        if language_id is not None:
            self.validate_language(language_id)
            url = url + '&lang=' + language_id
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


    def get_livescores_by_country(self, country_id, language_id):
        return self.get_all_livescores(country_id, language_id, None)

                
    def get_livescores_by_league(self, league_id, language_id):
        return self.get_all_livescores(None, language_id, league_id)

    '''def get_fixtrures(self, country_id, league_id, language_id, date):
        if country_id is not None:
            self.validate_country(country_id)
            url = url + '&country_id=' + country_id

        return []

    def get_fixtrures_by_country(self, country_id, language_id):
        return self.get_fixtrures(country_id, None, language_id, None)

    def get_todays_fixtures(self):
        return self.get_fixtrures(None, None, None, today())'''