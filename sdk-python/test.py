import requests
import json
import livescoreapi


def livescores_api():
    client = livescoreapi.Livescores('http://livescore-api.com/api-client/', '6r94GgdPiJ5ciqdx', '70Qx0KjZN2uD6jfdLohrFuhXem9wNm4U')
    livescores_data = client.get_all_livescores()
    #print(livescores_data)
    return livescores_data

def by_country():
    client = livescoreapi.Livescores('http://livescore-api.com/api-client/', '6r94GgdPiJ5ciqdx', '70Qx0KjZN2uD6jfdLohrFuhXem9wNm4U')
    country_livescores_data=client.get_livescores_by_country(71)
    return country_livescores_data

def by_league(league_id, language_id):
    client = livescoreapi.Livescores('http://livescore-api.com/api-client/', '6r94GgdPiJ5ciqdx', '70Qx0KjZN2uD6jfdLohrFuhXem9wNm4U')
    if language_id == "ar" or language_id == "fa" or language_id == "en" or language_id == "ru":
        league_livescores_data=client.get_livescores_by_league(league_id, language_id)
        return league_livescores_data
    else:
        language_id == "en"
        league_livescores_data=client.get_livescores_by_league(league_id, language_id)
        print("The lnguage was changed to English")
        return league_livescores_data

#r=livescores_api()
#print(r)
cntry=by_country()
print(cntry)
liga=by_league(218, "bg")
print(liga)