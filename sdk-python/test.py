import requests
import json
import livescoreapi

api_url = 'http://livescore-api.com/api-client/'
api_key = ''
api_secret = ''


def livescores_api(api_url,api_key,api_secret):
    client = livescoreapi.Livescores(api_url,api_key,api_secret)
    livescores_data = client.get_all_livescores()
    #print(livescores_data)
    return livescores_data

def by_country(api_url,api_key,api_secret, country_id, language_id):
    client = livescoreapi.Livescores(api_url,api_key,api_secret)
    country_livescores_data=client.get_livescores_by_country(country_id, language_id)
    return country_livescores_data

def by_league(api_url,api_key,api_secret, league_id, language_id):
    client = livescoreapi.Livescores(api_url,api_key,api_secret)
    league_livescores_data=client.get_livescores_by_league(league_id, language_id)
    return league_livescores_data
   

#r=livescores_api(api_url,api_key,api_secret)
#print(r)
cntry=by_country(api_url,api_key,api_secret, 12, "fa")
print(cntry)
liga=by_league(api_url,api_key,api_secret, 38, "bg")
print(liga)