from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
import json



app = Flask(__name__)

@app.route("/")
def test():
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
    print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    json_data = r.json()
    r.close()
    return render_template('home.php', json_data = json_data)

@app.route("/create")
def create():
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
    name = "test"
    flavor = "http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/flavors/2"
    image = "http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/images/326ea803-09f4-4129-bc87-8bdfd6e82525"
    #image = "326ea803-09f4-4129-bc87-8bdfd6e82525"
    adminPass = "ilkom"
    url = 'http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/servers'
    headers = {'content-type': 'application/json', 'X-Auth-Token':str(tokenid)}
    payloads = {'server':{'name': name, 'flavorRef':flavor, 'imageRef':image, 'adminPass':adminPass}}
    create = requests.post(url, data=json.dumps(payloads), headers=headers)
    #create = requests.get(url, headers=headers)
    json_data = create.json()
    print json.dumps(create.json(), sort_keys=True, indent=4, separators=(',', ': '))
    #print r.headers.get('content-type')
    #print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    json_data = create.json()
    create.close()

@app.route("/signup")
def signup():
    return 'sukses!'

if __name__ == "__main__":
    app.run()