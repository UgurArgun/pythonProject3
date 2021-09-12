import json
import allure_pytest
import pytest
import requests
import jsonpath
import logging
from Utils.config import LOG, BASE_URI

def test_ev():
    res= requests.get("https://api.test.virta-ev.com/v4/stations?"
                      "latMin=60.164101&"
                      "latMax=60.164104&"
                      "longMin=24&"
                      "longMax=25")
    code=res.status_code
    print(code)

    logging.info("logthis")
    assert res.headers["Content-Type"]=="application/json"
    json_response= res.json()
    print(json_response)
    assert json_response[0]["id"]==8617
    assert json_response[0]["name"]=="Test station advanced pricing"
    assert json_response[0]["city"]== "Helsinki"
    print(json_response [0]["latitude"])
    assert json_response[0]["longitude"]==24.899113

    name= json_response[0]["name"]
    print("name of the first: ", name)

    provider= json_response[0]["provider"]
    print("The best provider is", provider)
    assert json_response[0]["evses"][0]["connectors"][0]["type"]=="Mennekes"

    assert json_response[0]["isRemoved"]== False
    assert json_response[0]["isPrivate"]== False

def test_ev2():
    logging.info("logthis")
    BASE_URL= "https://api.test.virta-ev.com/v4"

    params= {'latMin':  8.658141, "latMax": 47.713408, "longMin": 24, "longMax": 25}

    response= requests.get(BASE_URL+ "/stations/", params=params)
    print(response)
    LOG.debug(response.json())
    resp= response.json()
    print("numbers of objects:", len(resp))

    ids= [d["id"] for d in resp]
    print(ids)

    cities= [d["city"] for d in resp]
    print(cities)

    connectors=[d["evses"][0]["connectors"][0]["type"] for d in resp]
    print(connectors)


def test_different_params():
    params = {'latMin': 29.077765, "latMax": 40.800505, "longMin": 2, "longMax": 3}

    response = requests.get(BASE_URI + "/stations/", params=params)

    code = response.status_code
    print(code)

    logging.info("logthis")
    assert response.headers["Content-Type"] == "application/json"
    json_response = response.json()
    print(json_response)
    assert json_response[-1]["id"] == 309381
    assert json_response[-1]["city"] == "Can Pastilla"
    assert json_response[-1]["address"]=="Carrer de la Goleta, 6C"
    assert json_response[-1]["longitude"] == 2.726626
    assert json_response[-1]["evses"][0]["connectors"][0]["type"] == "Mennekes"
    assert json_response[0]["isRemoved"] == False
    assert json_response[0]["isPrivate"] == False
