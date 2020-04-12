#!/usr/bin/env python
# coding utf-8
import pprint
import requests
from pymongo import MongoClient
import time

def read_remo():
    # Bearer XXXXX
    auth = ''
    response = requests.get(
        'https://api.nature.global/1/devices',
        headers={'accept': 'application/json', 'Authorization': auth})
    newest_events = response.json()[0]['newest_events']
    return {'humidity': newest_events['hu']['val'],
            'illuminance': newest_events['il']['val'],
            'temperature': int(float(newest_events['te']['val']) * 10)}

if __name__== '__main__':
    # mongodb
    client = MongoClient("mongodb://localhost:27017")
    db = client.dhmongo
    time_in_sec = 60
    while True:
      newest_events = read_remo()
      pprint.pprint(newest_events)
      # mongodb
      db.natureRemo.insert(newest_events)
      time.sleep(time_in_sec)