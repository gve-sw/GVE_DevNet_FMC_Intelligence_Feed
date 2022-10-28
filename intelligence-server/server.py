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

from flask import Flask, Response, send_from_directory
import logging
import urllib3
import pprint
from parser import check_to_txt, check

app = Flask(__name__, static_url_path='')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
pp = pprint.PrettyPrinter(indent=2)
# logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



@app.route('/url')
def get_url():
    check_to_txt()
    return send_from_directory('', 'url.txt')


@app.route('/ip')
def get_ip():
    check_to_txt()
    return send_from_directory('', 'ip.txt')


@app.route('/dns')
def get_dns():
    check_to_txt()
    return send_from_directory('', 'dns.txt')

@app.route('/webex', methods=['GET'])
def webex():
    data = check()
    if data != 'error':
        return data
    else:
        return Response("Page format has changed, please contact the developer", status=500, mimetype='application/json')


def main():
    app.run(host='0.0.0.0', port='5000', debug=True)


if __name__ == '__main__':
    main()
