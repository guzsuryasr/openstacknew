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
    userid = "clay"
    flavor = "m1.small"
    image = "ubuntu 16.04"
    adminPass = "ilkom"
    tenatid = "87db7a9811e94b4da15a4be421d5c566"
    url = 'http://172.16.160.110:5000/v2.0/tokens'
    headers = {'content-type': 'application/json'}
    payload = {'server':{'name': userid, 'flavorRef':flavor, 'imageRef':image 'adminPass':adminPass}}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return render_template('create.html')
   #return 'Hello, World!'

@app.route("/signup")
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run()
