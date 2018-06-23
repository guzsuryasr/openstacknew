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
json_data = r.json()
#data = json_data
#print data.id
#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
print json_data['servers'][0]['id']
json_data = r.json()
r.close()
