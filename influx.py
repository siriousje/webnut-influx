#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import json
from config import read_config
from influxdb import InfluxDBClient

# reads the yaml file and augments it with environment variables if they exist
def get_influx_config():
    config = read_config().get("influx")

    # augment the environment on top
    for key in ['hostname', 'port', 'username', 'password', 'database']:
        override = os.getenv("INFLUX_{}".format(key.upper()), config.get(key, None))
        if override is not None:
            config[key] = override

    return config

# read it as a global
influx_account = get_influx_config()

# writes the payload to the influxdb
def write_to_influxdb(payload):
    global influx_account
    # host, port, user, password, database
    influx_client = InfluxDBClient(influx_account['hostname'], influx_account['port'], influx_account['username'], influx_account['password'], influx_account['database'])
    influx_client.write_points(payload)


# if run as main, it will dump the output of your configuration
def main():
    config = get_influx_config()
    print(json.dumps(config, indent=4))

if __name__ == '__main__':
    main()