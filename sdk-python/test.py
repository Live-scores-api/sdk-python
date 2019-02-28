import requests
import json
import livescoreapi


def livescores_api():
    client = livescoreapi.Livescores('http://livescore-api.com/api-client/', '6r94GgdPiJ5ciqdx', '70Qx0KjZN2uD6jfdLohrFuhXem9wNm4U')
    livescores_data = client.get_all_livescores()
    #print(livescores_data)
    return livescores_data

r=livescores_api()
print(r)