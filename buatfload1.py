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
#name = "ilkom"
#lavor = "http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/flavors/2"
#image = "http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/images/326ea803-09f4-4129-bc87-8bdfd6e82525"
#adminPass = "ilkom"
#keyname = "keyspair"
pool = "nova"
url = 'http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/os-floating-ips'
headers = {'content-type': 'application/json', 'X-Auth-Token':str(tokenid)}
#payloads = {'server':{'name': name, 'flavorRef':flavor, 'imageRef':image, 'adminPass':adminPass, 'key_name':keyname}}
#payloads = {'pool': nova}
create = requests.post(url, data=json.dumps(pool), headers=headers)
#create = requests.get(url, headers=headers)
json_data = create.json()
print json.dumps(create.json(), sort_keys=True, indent=4, separators=(',', ': '))
#print r.headers.get('content-type')
#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
json_data = create.json()
create.close()
floatingss_ = json.loads(json.dumps(json_data))
floatingss_ip = floatingss_['floating_ip']['ip']
print floatingss_ip
#tokens = json.loads(json.dumps(json_data))
#print tokens
#tokenid = tokens['access']['token']['id']
#print tokenid