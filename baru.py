import os
import novaclient.v1_1.client as nvclient
from credential import get_nova_creds

def get_keystone_creds():
	d = {}
	d['admin'] = os.environ['ilkom']
	d['ilkom'] = os.environ['ilkom']
	d['http://172.16.160.110:5000/v2.0/'] = os.environ['http://172.16.160.110:5000/v2.0/']
	d['87db7a9811e94b4da15a4be421d5c566'] = os.environ['87db7a9811e94b4da15a4be421d5c566']
	return d

def get_nova_creds():
	d = {}
	d['admin'] = os.environ['ilkom']
	d['ilkom'] = os.environ['ilkom']
	d['http://172.16.160.110:5000/v2.0/'] = os.environ['http://172.16.160.110:5000/v2.0/']
	d['87db7a9811e94b4da15a4be421d5c566'] = os.environ['87db7a9811e94b4da15a4be421d5c566']
	return d

creds = get_nova_creds
nova = nvclient.Client(**creds)
print nova.servers.list()

try:
    creds = get_nova_creds()
    nova = nvclient.Client(**creds)
    image = nova.images.find(name="ubuntu 16.04")
    flavor = nova.flavors.find(name="m1.small")
    instance = nova.servers.create(name="coba", image=image, flavor=flavor, key_name=""
