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
    

        
                
    

