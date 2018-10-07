#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:39:23 2018

@author: shrey.aryan
"""

import urllib.request


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
    def __init__(self,key,secret):
        self.key = key 
        self.secret = secret 
    
    def _get_html_file(self,link):
        """returns the source code given a link"""
    
        try:
            html_file = urllib.request.urlopen(link)
            return html_file
        except Exception as e:
            print(str(e))
            
    def get_all(self):
        """returns all the livescores"""
        
        link = "http://livescore-api.com/api-client/scores/live.json?key={}&secret={}".format(self.key,self.secret)
        html_file = self._get_html_file(link)
        if html_file is not None: 
            json_data = html_file.read()
            return json_data
        
    
    
    
    
    

        
                
    

