#from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
import json

userid = "admin"
password = "ilkom"
tenatid = "87db7a9811e94b4da15a4be421d5c566"
url = 'http://172.16.160.110:5000/v2.0/tokens'
headers = {'content-type': 'application/json'}
payload = {'auth':{'passwordCredentials':{'username': userid, \
'password':password}, 'tenantId':tenatid}}
r = requests.post(url, data=json.dumps(payload), headers=headers)
#print r.headers.get('content-type')
#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
json_data = r.json()
r.close()
tokens = json.loads(json.dumps(json_data))
#print tokens
tokenid = tokens['access']['token']['id']
#print tokenid
url = 'http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/servers'
headers = {'X-Auth-Token':str(tokenid)}
r = requests.get(url, headers=headers)


def data():
	#tokenid = tokens['access']['token']['id']
	#print tokenid
	#url = 'http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/servers'
	#headers = {'X-Auth-Token':str(tokenid)}
	r = requests.post(url, headers=headers)
    name = "clay"
    flavor = "http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/flavors/2"
    image = "http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/images/326ea803-09f4-4129-bc87-8bdfd6e82525"
    image = "326ea803-09f4-4129-bc87-8bdfd6e82525"
    adminPass = "ilkom"
    headers = {'content-type': 'application/json'}
    payload = {'server':{'name': name, 'flavorRef':flavor, 'imageRef':image, 'adminPass':adminPass}}


if __name__ == "__main__":
    data()