import requests
import json


userid = "aa542589762c49079efc4768c6391337"
password = "ilkom"
#tenatid = "e73765c2080d4c038efc2acb094bbc1f"
url = 'http://172.16.160.110/v2.0/tenants'
headers = {'content-type': 'application/json'}
payload = {'auth':{'passwordCredentials':{'username': userid, \
        'password':password}, 'tenantId':''}}    
r = requests.post(url, data=json.dumps(payload), headers=headers)
print r.headers.get('content-type')
print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))