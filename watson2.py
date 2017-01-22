import os

import requests
import json
import math
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
        data = json.loads(response.text)
        needs = data["tree"]["children"][1]["children"][0]["children"]
        values = data["tree"]["children"][2]["children"][0]["children"]

        user_needs = {}
        user_values = {}

        for n in needs:
            user_needs[n["name"]] = round(float(n["percentage"])*100)
        for v in values:
            user_values[v["name"]] = round(float(v["percentage"])*100)

        return user_needs,user_values

    except:
        raise Exception("Error processing the request, HTTP: %d" %response.status_code)
