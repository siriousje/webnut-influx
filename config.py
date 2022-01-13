#!/usr/bin/python3
# -*- coding: utf-8 -*-

import yaml
import os
import json

config_location = "config.yml"

def read_config():
    global config_location
    try: 
        location = os.path.join(os.path.os.path.dirname(os.path.abspath(__file__)), config_location)
        config = {}
        with open(location, 'r') as file:
            try:
                loaded = yaml.load(file, Loader=yaml.FullLoader)
                if loaded is not None:
                    config = loaded
            except:
                print("unable to load config file from {config_location}, please check for valid yaml")
                exit(1)

    except:
        print(f"unable to open ./{config_location}, does it exist?")
        exit(1)

    return config


def main():
    print(json.dumps(read_config(), indent=4))

if __name__ == '__main__':
    main()

