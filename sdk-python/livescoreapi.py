#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:39:23 2018

@author: shrey.aryan
"""

import urllib.request
import requests


class Livescores:

    api_url = ''
    api_key = ''
    api_secret = ''

    def __init__(self, api_url, api_key, api_secret):
        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret

    
    def get_all_livescores(self):
       livescores = requests.get('{}scores/live.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret))
       return livescores.json()


    def validate_country(self, country_id):
        if (isinstance(country_id, str)):
            raise ValueError("Country ID must be a integer")
        elif country_id == None:
            return False
        elif country_id <= 0:
            raise ValueError("Wrong country ID")
        else: 
            return True
       
    def validate_language(self, language_id):
        if (isinstance(language_id, int)):
            raise ValueError("Language ID must be a string")
        elif language_id == None:
            return False
        elif language_id == "ar" or language_id == "fa" or language_id == "en" or language_id == "ru":
            return True
        else:
            print("The lnguage was changed to English") 
            return True          

    
    def get_livescores_by_country(self, country_id, language_id):
        url = '{}scores/live.json?key={}&secret={}'.format(self.api_url, self.api_key, self.api_secret)
        validate_ctry = self.validate_country(country_id)
        print(validate_ctry)
        if validate_ctry == True:
            url = url + '&country=' + str(country_id)
            print(url)
        validate_lang = self.validate_language(language_id)
        print(validate_lang)
        if validate_lang == True:
            url = url + '&lang=' + language_id
            print(url)
        country_livescore = requests.get(url)
        return country_livescore.json()

                
    def get_livescores_by_league(self, league_id, language_id):
        if league_id > 0:
            league_livescores = requests.get('{}scores/live.json?key={}&secret={}&league={}&lang{}'.format(self.api_url, self.api_key, self.api_secret, league_id, language_id))
            if language_id == "":
                league_livescores = requests.get('{}scores/live.json?key={}&secret={}&league={}'.format(self.api_url, self.api_key, self.api_secret, league_id))
                return league_livescores.json() 
            else:
                league_livescores = requests.get('{}scores/live.json?key={}&secret={}&league={}&lang{}'.format(self.api_url, self.api_key, self.api_secret, league_id, language_id))
                if language_id == "ar" or language_id == "fa" or language_id == "en" or language_id == "ru":
                    return league_livescores.json()
                else:
                    language_id == "en"
                    print("The lnguage was changed to English")    
                    return league_livescores.json()
        else:
            print("Wrong league ID!")