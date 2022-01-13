#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import urllib3
from bs4 import BeautifulSoup;
from influx import write_to_influxdb;
from config import read_config;
import datetime

metrics = [
    'battery.charge',
    'battery.runtime',
    'battery.voltage',
    'input.voltage',
    'input.voltage.nominal',
    'output.voltage'
]

def send_data_to_influx(timestamp: datetime.datetime, fields): 
    payload = [{
        "measurement": "ups_data",
        "time": timestamp,
        "fields": fields
    }]
    write_to_influxdb(payload)

def main():
    global metrics;
    url = read_config().get('webnut').get('url');
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    if response.status == 200:
        html = response.data.decode('utf-8')
        parser = BeautifulSoup(html, "lxml")
        rows = parser.select('table > tbody > tr')
        fields = {}
        timestamp = datetime.datetime.utcnow()

        for row in rows:
            cells = row.select('td')
            key = cells[0].text.strip()
            if key in metrics:
                value = cells[2].text.strip()
                fields[key] = float(value)
        send_data_to_influx(timestamp, fields)
    else:
        print(f"invalid status while requesting url ({response.status}, ignoring result")


if __name__ == '__main__':
    main()

