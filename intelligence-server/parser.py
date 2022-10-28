#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) 2022 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""


__author__ = "Josh Ingeniero <jingenie@cisco.com>"
__copyright__ = "Copyright (c) 2022 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


import pandas as pd
import json


def check():
    # Grab the latest Webex Teams information
    try:
        url_csv = pd.read_csv('https://www.ciscospark.com/content/dam/ciscospark/eopi/global/assets/Docs/spark_wsa.csv',
                              header=None)
        ip_url = pd.read_html('https://help.webex.com/en-us/article/WBX000028782/Network-Requirements-for-Webex-Teams-Services',
                              header=0, flavor='html5lib')
    except Exception as e:
        print(e)
        print("Page format has changed, please contact the developer")
        return('error')

    # Parsing the info
    url_list = url_csv[0].to_list()
    ip_list = []
    data = {}

    # Finding the appropriate table
    for table in ip_url:
        try:
            table['IP subnets for media services']
            break
        except KeyError:
            print(KeyError)
            # print(table)
            continue
        except Exception as e:
            print(e)
            print("Page format has changed, please contact developer")
            return 'error'

    # Convert table to list
    ip_width = len(table.columns)
    ip_list += table['IP subnets for media services'].to_list()
    for index in range(1, ip_width):
        ip_list += table[f'IP subnets for media services.{index}'].to_list()

    new_url_list = []
    dns_list = []

    for item in url_list:
        if item.startswith('.'):
            item = item.replace('.', '', 1)
        new_url_list.append(item)
    for item in url_list:
        if item.startswith('.'):
            item = item.replace('.', '*.', 1)
        dns_list.append(item)

    # Serialise to JSON
    data['URL'] = new_url_list
    data['IP'] = ip_list
    data['DNS'] = dns_list
    return data


def check_to_txt():
    data = check()

    with open('url.txt', 'w') as file:
        for item in data['URL']:
            file.write('%s\n' % item)
    with open('ip.txt', 'w') as file:
        for item in data['IP']:
            file.write('%s\n' % item)
    with open('dns.txt', 'w') as file:
        for item in data['DNS']:
            file.write('%s\n' % item)


if __name__ == '__main__':
    check_to_txt()
