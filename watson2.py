import os

import requests
import json
import pprint

def getProfile(text):
    url = "https://gateway.watsonplatform.net/personality-insights/api"
    username = "ae94b75a-bc86-4dc3-babe-715d6bc1a21e"
    password = "Vm8xAgu0KVZY"

    """Returns the profile by doing a POST to /v2/profile with text"""
    if url is None:
        raise Exception("No Personality Insights service is bound to this app")

    response = requests.post(url + "/v2/profile",auth=(username,password),headers={"content-type": "text/plain"},data=text)
    try:
        return json.loads(response.text)
    except:
        raise Exception("Error processing the request, HTTP: %d" %response.status_code)


f=open('archit.txt','r')
text=f.read()


pprint.pprint(getProfile(text))