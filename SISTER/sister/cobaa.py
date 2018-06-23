export OS_USERNAME=admin
export OS_PASSWORD=ilkom
export OS_TENANT_NAME='87db7a9811e94b4da15a4be421d5c566'
export OS_AUTH_URL='http://172.16.160.110:5000/v2.0'
export OS_COMPUTE_API_VERSION=2




from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client
loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(auth_url='http://172.16.160.110:5000/v2.0',
                                 username='admin',
                                 password='ilkom',
                                 project_id='87db7a9811e94b4da15a4be421d5c566')
sess = session.Session(auth=auth)
nova = client.Client(VERSION, session=sess)
