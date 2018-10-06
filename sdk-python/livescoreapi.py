#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:39:23 2018

@author: shrey.aryan
"""

import urllib.request


class livescores:
    
    def get_all(key,secret):
        html_file = urllib.request.urlopen("http://livescore-api.com/api-client/scores/live.json?key=" + key + "&secret=" + secret)
        json_data = html_file.read()
        return json_data
    

        
                
    

