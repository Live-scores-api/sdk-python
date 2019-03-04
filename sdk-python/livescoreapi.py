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
        if country_id <= 0:
            raise ValueError("Wrong country ID")
        else: 
            return True
       
    
    def get_livescores_by_country(self, country_id, language_id):
        validate = validate_country(country_id)
        print(validate)
        if language_id == "":
            country_livescores = requests.get('{}scores/live.json?key={}&secret={}&country={}'.format(self.api_url, self.api_key, self.api_secret, country_id))
            return country_livescores.json()
        else:
            country_livescores = requests.get('{}scores/live.json?key={}&secret={}&country={}&lang={}'.format(self.api_url, self.api_key, self.api_secret, country_id, language_id))
            if language_id == "ar" or language_id == "fa" or language_id == "en" or language_id == "ru":
                return country_livescores.json()
            else:
                language_id == "en"
                print("The lnguage was changed to English")    
                return country_livescores.json()
        
        
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