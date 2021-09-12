import json
import allure_pytest
import pytest
import assertpy
import requests
import jsonpath
from Utils.config import BASE_URI
from assertpy.assertpy import assert_that
from Utils.config import LOG


def test_api():
    #BASE_URL = "https://api.test.virta-ev.com/v4"

    params = {'latMin': 8.658141, "latMax": 47.713408, "longMin": 24, "longMax": 26}
    response = requests.get(BASE_URI + "/stations/", params=params)
    print (response)

    LOG.debug(response.json())
    jsonresp= response.json()
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.headers["Content-Type"]).is_equal_to("application/json")

    #Serialize ``obj`` to a JSON formatted ``str``
    print(json.dumps(jsonresp, indent=3))

    # print("json response", jsonresp)
    ids= [ev["id"] for ev in jsonresp]

    cities= [ev["city"] for ev in jsonresp]
    print(cities)

    provider= [ev["provider"] for ev in jsonresp]
    connectortype=[d["evses"][0]["connectors"][0]["type"] for d in jsonresp]
    print(connectortype)
    connectorkW=[d["evses"][0]["connectors"][0]["maxKw"] for d in jsonresp]

    print("list of connectors:", connectorkW)
    print("the last connector:", connectorkW[-1])

    # I can do assertions in different
    assert_that(ids).contains(184855)
    # id should be unique
    assert_that(ids).does_not_contain_duplicates()
    # city name can be duplicate
    assert_that(cities).contains_duplicates()
    assert_that(connectorkW[16]).is_greater_than(50)

    assert_that(cities).contains("Aachen")
    assert_that(provider).contains("Hubject")
    assert_that(provider).does_not_contain("Virta")
