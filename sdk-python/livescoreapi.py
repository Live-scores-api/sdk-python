#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:39:23 2018

@author: shrey.aryan
"""

import urllib.request
import json

class livescores:
    """
    A class used to get livescores. 
    ...

    Attributes
    ----------
    key : str
        an alphanumeric string used to access data from the LiveScore API
    secret : str
        an alphanumeric string used to access data from the LiveScore API
    
    Methods
    -------
    _get_html_file(link)
    
    get_all()
    
    """
    link_get_all = "http://livescore-api.com/api-client/scores/live.json?key={}&secret={}"
   
    def __init__(self, key, secret):
        
        try: 
            key.strip()
            secret.strip()
            assert len(key) == 16
            assert len(secret) == 32
            self.key = key
            self.secret = secret 
            
        except Exception as e:
            print("Key or Secret is Empty!")
    
    def _make_api_call(self, link):
        """returns the source code given a link"""
    
        try:
            http_response_object = urllib.request.urlopen(link)
            if http_response_object is not None: 
                json_string = http_response_object.read().decode('utf-8')
                json_dic = json.loads(json_string)
                return json_dic
            
        except urllib.error.HTTPError as e:
            print (str(e))
        
        except urllib.error.URLError as e:
            print (str(e))
        
        except urllib.error.ContentTooShortError as e:
            print (str(e))
            
    def get_all(self):
        """returns all the livescores"""
        link = self.link_get_all.format(self.key,self.secret)
        return self._make_api_call(link)
