import json
from urllib.request import urlopen


def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/" +
                       ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    print(responseJson)
    return responseJson.get("country_code")

print(getCountry("50.78.253.58"))

print(getCountry("90.221.2.194"))

print(getCountry("121.97.110.145"))
