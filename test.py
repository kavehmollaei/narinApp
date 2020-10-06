import os
from logging.handlers import RotatingFileHandler
import json,time,platform,subprocess,logging,requests,urllib3
from typing import Counter
from urllib3 import disable_warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


logging.basicConfig(format='%(asctime)s:>>>>%(message)s',level=logging.DEBUG ,filename='log-test.log',filemode='a')


#build header
headers={}
headers['content-type'] = 'application/json'
headers['Accept'] = 'application/json'
with open('urls.json') as data:
    api_urls = json.load(data)

out = open('file.txt', 'w')

login_data = {'username': 'admin', 'password': 'admin'}


# send request for get login token
req = requests.post('https://192.168.4.164/api-token-auth/',data=json.dumps(login_data),verify=False,headers=headers)
token=req.content.decode()
token_json=json.loads(token)
# print(token_json)


# add token to the header
headers['Authorization']= f"Token {token_json['token']}"


url_site_to_site_restart = 'https://192.168.4.164/api/vpn/site-to-sites/2/restart'
response_restart_tunnel = requests.patch(url_site_to_site_restart,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=20)
if response_restart_tunnel.ok:
    print('reset succesfully')



def Get_Route(url_route, input_timeout=10):
    try:
        response_show_routeing_table = requests.get(url_route, headers={
                                                    'Authorization': 'Token '+token_json['token']}, verify=False, timeout=input_timeout)
        result_route_json = response_show_routeing_table.json()
        # print(result_route_json.get('count'))
        logging.info('Get {} Routes'.format(result_route_json.get('count')))
        out.write('\n')
        out.write(
            'Count of routes:--->>> {}'.format(str(result_route_json.get('count'))))
        print('Count of routes:--->>> {}'.format(result_route_json.get('count')))

        route_count = int(result_route_json['count'])
        out.write('\n')
        # print(result_route_json['results'])
        for i in range(0, route_count):
            # print(result_route_json['results'][i]['interface']['mac'])
            out.write('Name : {}'.format(
                result_route_json['results'][i]['name']))
            out.write('\n')
            # out.write('Name : {}'.format(result_route_json['results'][i]['name']))
            out.write('\n')
            print('Name : {}'.format(result_route_json['results'][i]['name']))
            out.write('Destination_Ip : {}'.format(
                result_route_json['results'][i]['destination_ip']))
            out.write('\n')
            print('Destination_Ip : {}'.format(
                result_route_json['results'][i]['destination_ip']))

            out.write('Destination_Mask: {}'.format(
                result_route_json['results'][i]['destination_mask']))
            out.write('\n')
            print('Destination_Mask: {}'.format(
                result_route_json['results'][i]['destination_mask']))
            out.write('Gateway: {}'.format(
                result_route_json['results'][i]['gateway']))
            out.write('\n')
            print('Gateway: {}'.format(
                result_route_json['results'][i]['gateway']))
            # print(result_route_json['results'][i]['interface']['name'])
            if result_route_json['results'][i]['interface'] is not None:
                out.write('Name of Interface: {}'.format(
                    result_route_json['results'][i]['interface']['name']))
                print('Name of Interface: {}'.format(
                    result_route_json['results'][i]['interface']['name']))
            else:
                out.write('\n')
                out.write('Interface is Null')
                out.write('\n')
                print('Interface is Null')
            print('Description: {}'.format(
                result_route_json['results'][i]['description']))
            print(
                '========================================================================================')
        return True
    except ConnectionError as error:
        print('Connection Not Found---->>>> {}'.format(error))
    return False


url_route = api_urls['api_route']
if not Get_Route(url_route):
    Get_Route(url_route, 20)




""" 
##  Get Firewall input

url_firewal_input = 'https://192.168.4.164/api/input-firewall/inputpolicies?offset=0&limit=10&ordering=name&real=true'

response_firewall_input = requests.get(url_firewal_input,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=20)
response_json_firewall_input=response_firewall_input.json()
print('Count of firewall input rules--->>>\t{}'.format(response_json_firewall_input.get('count')))
print(response_json_firewall_input.get('count'))

for i in range(0,response_json_firewall_input.get('count')-1):

        # print(response_json_firewall_input.get('results')[i]['source'])
    if response_json_firewall_input.get('results')[i]['source'] is not None:
        # print(response_json_firewall_input.get('results')[i])
        # response_json_firewall_input.get('results')[i]['source']['src_interface_list']==[]:
        if response_json_firewall_input.get('results')[i]['permission']=='admin':

            print('Name of Input rule: {}'.format(response_json_firewall_input.get('results')[i]['name']))
            count_interface = len(response_json_firewall_input.get('results')[i]['source']['src_interface_list'])
        
        # print(count_interface) 

        for item in range(count_interface):
            print('In interfaces {}\t:{}'.format(item,response_json_firewall_input.get('results')[i]['source']['src_interface_list'][item]['name']))
        print('Service List: {}'.format(response_json_firewall_input.get('results')[i]['service_list']))
        print('is_log_enabled: {}'.format(response_json_firewall_input.get('results')[i]['is_log_enabled']))
        print('Description: {}'.format(response_json_firewall_input.get('results')[i]['description']))
        print('Status: {}'.format(response_json_firewall_input.get('results')[i]['status']))
        print('=========================================================')

'''
'''
# Get site to site vpn

url_site_to_site='https://192.168.4.164/api/vpn/site-to-sites?offset=0&limit=10&ordering=name&real=true'
response_vpn_input = requests.get(url_site_to_site,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=20)
response_vpn_input_json = response_vpn_input.json()
print(response_vpn_input_json)
print('count of ipsec Tunnels: \t{}'.format(response_vpn_input_json.get('count')))
tunel_count = response_vpn_input_json.get('count')

for i in range(tunel_count):
    print('Is Enable:\t{}'.format(response_vpn_input_json.get('results')[i].get('is_enabled')))
    print('Name of Ipsec tunnel:\t{}'.format(response_vpn_input_json.get('results')[i].get('name')))
    print('Local network:{}'.format(response_vpn_input_json.get('results')[i].get('local_network')))
    print('Remote network:{}'.format(response_vpn_input_json.get('results')[i].get('remote_network')))
    print('Local Service network:{}'.format(response_vpn_input_json.get('results')[i].get('local_service_list')))
    print('Remote Service network:{}'.format(response_vpn_input_json.get('results')[i].get('remote_service_list')))
    print('Local Id:{}'.format(response_vpn_input_json.get('results')[i].get('local_id')))
    print('Peer Id:{}'.format(response_vpn_input_json.get('results')[i].get('peer_id')))
    print('phase1_authentication_algorithm:\t{}'.format(response_vpn_input_json.get('results')[i].get('phase1_authentication_algorithm')))
    print('phase2_authentication_algorithm:\t{}'.format(response_vpn_input_json.get('results')[i].get('phase2_authentication_algorithm')))
    print('phase1_encryption_algorithm:\t{}'.format(response_vpn_input_json.get('results')[i].get('phase1_encryption_algorithm')))
    print('phase2_encryption_algorithm:\t{}'.format(response_vpn_input_json.get('results')[i].get('phase2_encryption_algorithm')))
    print('phase1_diffie_hellman_group:\t{}'.format(response_vpn_input_json.get('results')[i].get('phase1_diffie_hellman_group')))
    print('phase2_diffie_hellman_group:\t{}'.format(response_vpn_input_json.get('results')[i].get('phase2_diffie_hellman_group')))
    print('authentication_method:\t{}'.format(response_vpn_input_json.get('results')[i].get('authentication_method')))
    print('preshared_key:\t{}'.format(response_vpn_input_json.get('results')[i].get('preshared_key')))
    print('dead peer detection:\t{}'.format(response_vpn_input_json.get('results')[i].get('dpd')))
    print('On Demand:\t{}'.format(response_vpn_input_json.get('results')[i].get('is_on_demand')))
    print('Description:\t{}'.format(response_vpn_input_json.get('results')[i].get('description')))
    print('Status Vpn:\t{}'.format(response_vpn_input_json.get('results')[i].get('vpn_connection_status')))
    
    print('=================================================================================')

#################################################################
'''

'''
# import pdb

# pdb.set_trace()
## tell me about about backup

url_Syslog = 'https://192.168.4.164/api/config/log_servers?offset=0&limit=10&ordering=address&real=true'
response_Syslog = requests.get(url_Syslog,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=20)
response_Syslog_json=response_Syslog.json()

print(response_Syslog_json)
print(response_Syslog_json.get('count'))
print(response_Syslog_json.get('results'))
# r = requests.get(google,headers=headers,allow_redirects=True)
# print(r.headers.keys())
# for i in r.headers.values():
    # print(i)
# print(r.is_redirect)
# print(r.history[2].headers)
# print(r.status_code)
# print(r.headers)

'''

'''
def creating_rotating_log(path):

    logger = logging.getLogger('root')
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(path,mode='a',maxBytes=10,delay=0,encoding=None)
    logger.addHandler(handler)
    while True:
        time.sleep(0.3)
        logger.info('dfdfdfdfdgsfagasgasfgfasg')

# creating_rotating_log('testrotatfile.log')        
       







# محاسبه حجم فایل

filename = 'testrotatfile.log'
with open(filename) as f:
    size=f.seek(0,2)
print(size)    
file = 'testrotatfile.log'
size_file = os.path.getsize(file)

print(size_file)





#get_data_json=r.json()
# print(get_data_json)
# print(get_data_json['response']['docs'])
#docs=get_data_json['response']['docs']
# print(docs)
# print(type(docs))
#print(json.dumps(docs))
#print(type(json.dumps(docs)))
##print(type(json_pac))
##json_pac_t = json.loads(json_pac)
##print(json_pac_t)
# json_pac=r.json()

##print(type(json_pac_t))
# print(json_pac)
# print(r.content)
# print(json_pac[0]['id'])

# print(type(json_pac[0]['id']))




# print(json.dumps(json_pac))




def myfunc(*args):
    total=0
    for i in args:
        total+=i
    return total    


print(myfunc(5,3,4,12,4,9))        




def append_new_line(file_name, text_to_append):
    Append given text as a new line at the end of file

    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)

append_new_line('sample3.txt', 'This is f')       
 """