import os
import time
import novaclient.v1_1.client as nvclient
from credential import get_nova_creds

try:
    creds = get_nova_creds()
    nova = nvclient.Client(**creds)
    image = nova.images.find(name="ubuntu 16.04")
    flavor = nova.flavors.find(name="m1.small")
    instance = nova.servers.create(name="coba", image=image, flavor=flavor, key_name="brbr"

    print ("Sleeping for 5s after create command")
    time.sleep(5)
    print ("List of Vms")
    print (nova.servers.list())

finally:
	print ("execution completed")