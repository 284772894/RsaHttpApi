__author__ = 'Rocky'

import urllib.request
import urllib.parse
import http.client
import json
HTTP = 'http://'


def request(base_url='dealer.kela.cn', port=36882, api='/RetailService/CAPI.aspx', params="", method="POST"):
    print(HTTP + base_url + api)
    try:
        http_params = urllib.parse.urlencode(params)
        http_headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Connection': 'Keep-Alive',
                        'Referer': HTTP + base_url, 'Accept': 'text/plain'}
        http_conn = http.client.HTTPConnection(base_url, port)
        http_conn.request(method=method, url=api, body=http_params, headers=http_headers)
        http_response = http_conn.getresponse()
        if http_response.status == 200:
            return http_response.read().decode('utf-8')
        else:
            return None
    finally:
        http_conn.close()
