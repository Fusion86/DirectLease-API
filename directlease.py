import hashlib
from uuid import uuid4
import requests
from time import time
from datetime import datetime
from urllib.parse import urlparse


BASE_URL = "https://tankservice.app-it-up.com/Tankservice/v2"

# All the values below can be whatever you want, these are just the 'official' values.
VERSION = 45
LANG = "nl"
IDENTIFIER = datetime.today().strftime("%Y%m%d") + "_" + str(uuid4())


def calculate_checksum(url: str):
    url_obj = urlparse(url)

    # Timestamp is not actually used, so it can be whatever you want.
    ts = int(time())

    var19 = f"{url_obj.path}?{url_obj.query}"
    var17 = f"{IDENTIFIER}/{ts}/"
    check_input = f"{IDENTIFIER}/{ts}/{var19}/X-Checksum"
    hash_object = hashlib.sha1(bytes(check_input, "UTF-8"))
    return var17 + hash_object.hexdigest()


def get_place(id: int):
    url = f"{BASE_URL}/places/{id}?_v={VERSION}&lang={LANG}"
    checksum = calculate_checksum(url)
    res = requests.get(url, headers={"X-Checksum": checksum})
    return res.json()


def get_places(northLat, eastLng, southLat, westLng, fuel):
    url = f"{BASE_URL}/places?country=NL&country=BE&northLat={northLat}&eastLng={eastLng}&southLat={southLat}&westLng={westLng}&fuel={fuel}&_v={VERSION}&lang={LANG}"
    checksum = calculate_checksum(url)
    res = requests.get(url, headers={"X-Checksum": checksum})
    return res.json()


# Example
res = get_places(52.556497, 5.182295, 52.132801, 4.634756, "euro95")
avg_price = res["avgPrice"]

print("avg_price =", avg_price)

place = res["places"][0]
print("some place")
print(place)

# or
res = get_place(place["id"])
print("get_place result")
print(res)
