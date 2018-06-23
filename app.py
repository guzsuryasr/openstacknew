from flask import Flask, render_template, json, request
from werkzeug import generate_password_hash, check_password_hash
import requests
import json

app = Flask(__name__)


def getid():
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
	#print json_data['servers'][0]['id']
	json_data = r.json()
	r.close()
	server_id = json_data['servers'][0]['id']
	return json_data['servers'][0]['id']

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/create',methods=['POST'])
def create():
    if request.method == 'POST':
    	userid = "admin"
    	password = "ilkom"
    	tenatid = "87db7a9811e94b4da15a4be421d5c566"
    	url = 'http://172.16.160.110:5000/v2.0/tokens'
    	headers = {'content-type': 'application/json'}
    	payload = {'auth':{'passwordCredentials':{'username': userid, 'password':password}, 'tenantId':tenatid}}
    	r = requests.post(url, data=json.dumps(payload), headers=headers)
    	json_data = r.json()
    	r.close()
    	tokens = json.loads(json.dumps(json_data))
    	tokenid = tokens['access']['token']['id']
        name = request.form['nm']
        flavor = "http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/flavors/2"
        image = "http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/images/326ea803-09f4-4129-bc87-8bdfd6e82525"
        adminPass = "ilkom"
        keyname = "keyspair"
        url = 'http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/servers'
        headers = {'content-type': 'application/json', 'X-Auth-Token':str(tokenid)}
        payloads = {'server':{'name': name, 'flavorRef':flavor, 'imageRef':image, 'adminPass':adminPass, 'key_name':keyname}}
        create = requests.post(url, data=json.dumps(payloads), headers=headers)
        json_data = create.json()
        print json.dumps(create.json(), sort_keys=True, indent=4, separators=(',', ': '))
        json_data = create.json()
        create.close()
        #server_id = json_data['server']['id']
        #print server_id
        #url = 'http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/servers/'+server_id
        #headers = {'X-Auth-Token':str(tokenid)}
        #r = requests.get(url, headers=headers)
        #json_data = r.json()
        #print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
        json_data = r.json()
        r.close()
        return render_template('home.html', json_data = json_data)

@app.route('/all_list')
def all_list():
	userid = "admin"
	password = "ilkom"
	tenatid = "87db7a9811e94b4da15a4be421d5c566"
	url = 'http://172.16.160.110:5000/v2.0/tokens'
	headers = {'content-type': 'application/json'}
	payload = {'auth':{'passwordCredentials':{'username': userid, \
	    'password':password}, 'tenantId':tenatid}}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	json_data = r.json()
	r.close()
	tokens = json.loads(json.dumps(json_data))
	tokenid = tokens['access']['token']['id']
	url = 'http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/servers/detail'
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	#d_retrieve = json.loads(json.dumps(json_data))
	#id_code = id_retrieve['id']
	#json_data = get_id_server(id_code) #buat ambil ID server
	json_data = r.json()
	r.close()
	return render_template('create_floating.html', json_data = json_data)


@app.route('/list')
def list():
	server_id = getid()
	userid = "admin"
	password = "ilkom"
	tenatid = "87db7a9811e94b4da15a4be421d5c566"
	url = 'http://172.16.160.110:5000/v2.0/tokens'
	headers = {'content-type': 'application/json'}
	payload = {'auth':{'passwordCredentials':{'username': userid, \
	    'password':password}, 'tenantId':tenatid}}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	json_data = r.json()
	r.close()
	tokens = json.loads(json.dumps(json_data))
	tokenid = tokens['access']['token']['id']
	url = 'http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/servers/'+server_id
	headers = {'X-Auth-Token':str(tokenid)}
	r = requests.get(url, headers=headers)
	json_data = r.json()
	print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	#d_retrieve = json.loads(json.dumps(json_data))
	#id_code = id_retrieve['id']
	#json_data = get_id_server(id_code) #buat ambil ID server
	json_data = r.json()
	r.close()
	return render_template('list.html', json_data = json_data)
#def get_id_server(server_id):
#	return server_id #simpan ID server

@app.route('/get_id', methods=['GET']) #{} buat ambil ID server
def get_id():
	if request.method == 'POST':
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
		return render_template('list2.html', json_data = json_data)
	#return 'helloworld {{server_id}}'


def addfload():
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
	public = "%s" %(floatingss_ip)
	private = "192.168.1.30"
	url = 'http://172.16.160.110:8774/v2/87db7a9811e94b4da15a4be421d5c566/servers/5e68409f-27b4-452e-a73e-bd27904e4f64/action'
	headers = {'content-type': 'application/json', 'X-Auth-Token':str(tokenid)}
	#payloads = {'server':{'name': name, 'flavorRef':flavor, 'imageRef':image, 'adminPass':adminPass, 'key_name':keyname}}
	payloads = {'addFloatingIp':{'address': public, 'fixed_address ':private}}
	create = requests.post(url, data=json.dumps(payloads), headers=headers)
	#create = requests.get(url, headers=headers)
	json_data = create.json()
	print json.dumps(create.json(), sort_keys=True, indent=4, separators=(',', ': '))
	#print r.headers.get('content-type')
	#print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
	json_data = create.json()
	create.close()

if __name__ == "__main__":
    app.run(debug = True, host = "127.0.0.1", port=5028)
