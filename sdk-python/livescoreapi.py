#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:39:23 2018

@author: shrey.aryan
"""

from urllib.parse import urlencode
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
    parent_link = "http://livescore-api.com/api-client"

   
    def __init__(self, key, secret):
        key.strip()
        secret.strip()
        
        if len(key) == 16:
            raise Exception('length of key should not be different from 16. The current length of key is: {}'.format(len(key)))
        if len(secret) == 32:
            raise Exception('length of secret should not be different from 32. The current length of secret is: {}'.format(len(secret)))

        self.key = key
        self.secret = secret 
        

    def get_auth(self):
        return urlencode({'key': self.key, 'secret': self.secret})
        
    
    def _make_api_call(self, endpoint):
        """returns the source code given a link"""
        
        try:
            http_response_object = urllib.request.urlopen(parent_link + endpoint +  '?' + urlli + self.get_auth())
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
        endpoint = "/scores/live.json"
        return self._make_api_call(endpoint)
