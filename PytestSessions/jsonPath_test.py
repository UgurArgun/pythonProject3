import json
import logging
import jsonpath
import requests
from Utils.config import BASE_URI
from jsonpath_ng import jsonpath, parse

def test_jsonpath_for_ev():

        params = {'latMin': 25.737473, "latMax": 66.486099, "longMin": 22, "longMax": 24}

        response = requests.get(BASE_URI + "/stations/", params=params)

        json_data = json.loads(response.text)

        print("Json response=", json_data)

        # get all cities
        jsonpath_expression = parse( "$.[*].'city'")

        cityList= [match.value for match in jsonpath_expression.find(json_data)]
        print("List of cities: ", cityList)

        # get all providers
        jsonpath_pro = parse("$.[*].'provider'")

        providersList = [match.value for match in jsonpath_pro.find(json_data)]
        print("List of providers: ", providersList)

        # logging
        logging.info("logthis")

        #some assertions
        assert providersList.__contains__("Virta")
        assert cityList.__contains__("Tampere Keskus")