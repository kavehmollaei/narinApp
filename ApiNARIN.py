import json,time,platform,subprocess,logging,urllib3,requests
from requests.packages.urllib3 import Retry
from subprocess import check_output
from logging.handlers import RotatingFileHandler
from urllib3 import disable_warnings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(format='%(asctime)s:>>>>%(message)s',
                    level=logging.DEBUG, filename='log-test.log', filemode='a')

# build header
headers = {}
headers['content-type'] = 'application/json'
headers['Accept'] = 'application/json'
login_data={'username':'admin','password':'admin'}
with open('urls.json') as data:
    api_urls = json.load(data)

#GET TOKEN
def get_Token(Token_Get):


# send request for get login token
    req = requests.post(Token_Get,
                        data=json.dumps(login_data), verify=False, headers=headers)
    token = req.content.decode()
    token_json = json.loads(token)
# print(token_json)
    return token_json

# add token to the header
    headers['Authorization'] = f"Token {token_json['token']}"
# print(headers)


api_Token=api_urls['api_Token']
token_json = get_Token(api_Token)

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
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


out=open('file.txt','w')


###############################################
# Get cpu informations


def Get_Cpuinfo():
    command = "lscpu"
    all_info = subprocess.check_output(command, shell=True).strip().decode()
    # print(all_info.split('\n'))
    for line in all_info.split('\n'):
        print(line)
        out.write(line)
        out.write('\n')
        
Get_Cpuinfo()

out.write('\n \n')
out.write('===>>')
##############################################################


# Get memory information
def Get_Memoryinfo():
    command = "free -h"
    all_info = subprocess.check_output(command, shell=True).strip().decode()
    print(all_info.split('\n'))
    for i in all_info.split('\n'):
        out.write(i)
        out.write('\n')
        print(i)
print('=====================================================================================')

Get_Memoryinfo()
out.write('\n \n')
#######################################################################



def Get_Config_Real_interfaces(url_interfaces, input_timeout=10):

    # get token result you can Un comment this for see token
    # print(token_json['token'])
    try:
        # global token_json
        # send request for show interfaces
        response_show_interface = requests.get(url_interfaces, headers={
                                               'Authorization': 'Token '+token_json['token']}, verify=False, timeout=input_timeout)
    # decode response
        response_show = response_show_interface.content.decode()

    # see type of response_show
    # print(type(response_show))

    # count of interfaces
        t = json.loads(response_show)
        count_of_interfaces = len(t.get('results'))
        #count of interfaces in file
        out.write('\n\n')
        out.write('Count of interfaces===>>{}'.format(str(count_of_interfaces)))
        out.write('\n')
        print('count_of_interfaces:{}'.format(count_of_interfaces))
    # print(t['results'][1])
        
       
        print('=====================================================================')
    
    
    # get interface informations
        for i in range(0, count_of_interfaces):
            print('DHCP_STATUS ETH{}----->'.format(i) +
                  str(t['results'][i]['is_dhcp_enabled']))
           
            out.write('DHCP_STATUS ETH{}----->'.format(i) + str(t['results'][i]['is_dhcp_enabled']))      
            out.write('\n')
            
            print('IP_LIST_ETH{}----->'.format(i) +
                  str(t['results'][i]['real_ip_list']))
            out.write('IP_LIST_ETH{}----->'.format(i) +str(t['results'][i]['real_ip_list']))
            out.write('\n')
            print('ETH{} was ---->'.format(i)+t['results'][i]['status'])
            out.write('ETH{} was ---->'.format(i)+t['results'][i]['status'])
            out.write('\n')
            print('LINK_TYPE ETH{}----->'.format(i) +
                  str(t['results'][i]['link_type']))
            out.write('LINK_TYPE ETH{}----->'.format(i) +str(t['results'][i]['link_type']))
            out.write('\n')
            
            print('TYPE WAN OR LAN ETH{}----->'.format(i) +
                  str(t['results'][i]['type']))
            out.write('TYPE WAN OR LAN ETH{}----->'.format(i) +
                  str(t['results'][i]['type']))
            out.write('\n')            
            print('Default Gateway is :----->',str(t['results'][i]['gateway']))
            out.write('\n')
            out.write('Default Gateway is :----->'+
                  str(t['results'][i]['gateway']))      
            out.write('\n')
            print('==============================================================')
        return True

    except ConnectionError as error:
        print('Connection not found--->>>{}'.format(error))
    return False




url_interfaces = api_urls['api_real_interfaces']



if not Get_Config_Real_interfaces(url_interfaces):
    Get_Config_Real_interfaces(url_interfaces, 20)


def Get_Route(url_route, input_timeout=10):
    try:
        response_show_routeing_table = requests.get(url_route, headers={
                                                    'Authorization': 'Token '+token_json['token']}, verify=False, timeout=input_timeout)
        result_route_json = response_show_routeing_table.json()
        logging.info('Get {} Routes'.format(result_route_json.get('count')))
        out.write('\n')
        out.write('Count of routes:--->>>{}'.format(str(result_route_json.get('count'))))
        print('Count of routes:--->>>'.format(result_route_json.get('count')))
        
        route_count = int(result_route_json['count'])
        out.write('\n')        
        # print(result_route_json['results'])
        for i in range(0, route_count):
            # print(result_route_json['results'][i]['interface']['mac'])
            out.write('Name : {}'.format(result_route_json['results'][i]['name']))
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
        print('Connection Not Found---->>>>{}'.format(error))
    return False


url_route = api_urls['api_route']
if not Get_Route(url_route):
    Get_Route(url_route, 20)


def Get_vlans(url_vlan, input_timeout=10):
    try:
        response_show_vlan = requests.get(url_vlan, headers={
                                          'Authorization': 'Token '+token_json['token']}, verify=False, timeout=input_timeout)
        response_show_json = response_show_vlan.json()
        logging.info('Get {} Vlans'.format(response_show_json['count']))
        
        print('Vlan_Counts:{}'.format(response_show_json['count']))
        count_vlan = response_show_json['count']
        if count_vlan == 0:
            print('Vlan Not Exist')
        else:
            # print(response_show_json)
            for i in range(0, count_vlan):
                print('Vlan Name: {}'.format(
                    response_show_json['results'][i]['name']))
                print('Vlan Ip: {}'.format(
                    response_show_json['results'][i]['ip_list']))
                print('Vlan Id: {}'.format(
                    response_show_json['results'][i]['data'][i]['vlan_id']))
        return True
    except ConnectionError as e:
        logging.error('Connection Not Found---->>>>{}'.format(e))
        print('Connection Not Found---->>>>{}'.format(e))
    return False


urll_vlan = api_urls['api_vlan']
if not Get_vlans(urll_vlan):
    Get_vlans(urll_vlan, 20)
print('=====================================================================')


# Get addressess objects
def Get_addresses_objects(url_addresses_objects, input_timeout=10):
    try:
        response_object_addresses = requests.get(url_addresses_objects, headers={
                                               'Authorization': 'Token '+token_json['token']}, verify=False, timeout=input_timeout)
        logging.info('Connection Established')
        response_objects_addresses_json = response_object_addresses.json()
        # get count
        count_addresss = response_objects_addresses_json['count']
        logging.info('Getting count')
        time.sleep(2)
        # count of object
        logging.info(f'Count of objects:{count_addresss}')
        print('Count of objects:', count_addresss)
        for i in range(count_addresss):
            print('list of object{}:{}'.format(response_objects_addresses_json.get('results')[i].get('id'), response_objects_addresses_json.get('results')[i]))
        logging.info('Gathering data done')
        return True
    except Exception as e:
        print('Connection not Found--->>>{}'.format(e))
        logging.error('Connection not Found--->>>{}'.format(e))
    return False

urll_addresses = api_urls['api_addresses']
if not Get_addresses_objects(urll_addresses):
    Get_addresses_objects(urll_addresses, 20)


# TODO: add address objects in test.py






'''
# Get address objects
url_objects_address = 'https://192.168.4.164/api/entity/addresses?offset=0&limit=10&ordering=name'
response_objects_address = requests.get(url_objects_address,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=20)
response_objects_address = response_objects_address.content.decode()
response_objects_address_json = json.loads(response_objects_address)

count_addresss = response_objects_address_json['count']
# print(count_addresss)

# print(response_objects_address_json['results'])

'''

##Get services

def Get_services(url_services,input_timeout=10):

    try:
        url_service='https://192.168.4.164/api/entity/services?offset=0&limit=9999'
        response_service=requests.get(url_services,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=20)
        response_result=response_service.json()
        logging.info('Gathering services')
        # Get count of services
        count_services=response_result.get('count')
        
        #Get count of services defined by admin
        count=0
        for i in range(count_services):
            is_user_define = response_result.get('results')[i].get('is_user_defined')
            if is_user_define== True:
                count +=1 
        print('count services define by admin:{}'.format(count))
        # Print results
        logging.info('Printing Results')
        print(response_result.get('results'))
        print('===============================================================')
        return True    
    except Exception as e:
        logging.error('connection Field: {}'.format(e))
    return False

url_services=api_urls.get('api_services')
if not Get_services(url_services):
    Get_services(url_services,20)


def Get_Backup(url_backup,input_timeout=10):
    try:
        response_backup = requests.get(url_backup,headers={
                                               'Authorization': 'Token '+token_json['token']}, verify=False, timeout=input_timeout)
        response_backup_json=response_backup.json()
        # print(response_backup_json)
        count_bak = response_backup_json.get('count')
        print('Count of Backups:{}'.format(count_bak))
        result_backup = response_backup_json.get('results')
        print('List of backups: {}'.format(result_backup))
        logging.info('Printing Backup info Results...')
        print('=========================================')
        return True
    except Exception as err:
        print('Connection Feild ==>> {} '.format(err))
        logging.error('connction Field: {}'.format(err))
    return False        
url_backup = api_urls['api_backup']
if not Get_Backup(url_backup):
    Get_Backup(url_backup,20)



def Get_ntp_servers(url_ntp,input_timeout=10):
    try:
        response_ntp = requests.get(url_ntp,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=input_timeout)
        response_ntp_json = response_ntp.json()
        logging.info('Gettig ntp objects...')
        print('Count of Ntp servers: {}'.format(response_ntp_json.get('count')))
        NtpServersList=response_ntp_json.get('results')[0].get('ntp_server_list')
        print('Results: {}'.format(NtpServersList))
        NtpServerEnable = response_ntp_json.get('results')[0].get('is_enabled')
        print('Is Enable:{}'.format(NtpServerEnable))
        NtpServerStatus = response_ntp_json.get('results')[0].get('status')
        print('Ntp Status: {}'.format(NtpServerStatus))
        host = NtpServersList[0]
        with open ('output.txt','w') as f:
            s=subprocess.run(['ping -c5 {}'.format(host)],shell=True,stderr=subprocess.DEVNULL,stdout=f)
            if s.returncode !=0:
                print('NTP Server is Unreachable')
            else:
                print('Ntp server is alive...')
        
        # print(response_ntp_json.get('results'))
        logging.info('Getting Results...')
        print('====================================================================')
        return True
    except Exception as err:
        print('Connection Feild ==>> {} '.format(err))
        logging.error('Connection Feild ==>> {} '.format(err))    
    return False

url_ntp = api_urls['api_ntp']
# Get_ntp_servers(url_ntp,20)

if not Get_ntp_servers(url_ntp):
    Get_ntp_servers(url_ntp,10)




        
def Get_Update_Manager(url_UpdateManager,input_timeout=10):
    try:
        response_Update_Manager = requests.get(url_UpdateManager,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=input_timeout)        
        response_Update_Manager_json = response_Update_Manager.json()
        print('update manager status: {}'.format(response_Update_Manager_json.get('results')[0].get('is_update_enabled')))
        Ip_UpdateServer=response_Update_Manager_json.get('results')[0].get('update_server')
        print('Update Server : {}'.format(Ip_UpdateServer))
        return True
    except Exception as err:    
        print(err)
    return False

  
url_UpdateManager=api_urls['api_update_manager']
if not Get_Update_Manager(url_UpdateManager):
    Get_Update_Manager(url_UpdateManager,20)
print('=========================================================================')

def Get_firewall_Input(url_firewall_input,input_timeout=10):
    try:

        response_firewall_input = requests.get(url_firewall_input,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=input_timeout)
        response_json_firewall_input=response_firewall_input.json()
        print('Count of firewall input rules--->>>\t{}'.format(response_json_firewall_input.get('count')))
        print(response_json_firewall_input.get('count'))

        for i in range(0,response_json_firewall_input.get('count')-1):

            if response_json_firewall_input.get('results')[i]['source'] is not None:
                if response_json_firewall_input.get('results')[i]['permission']=='admin':
                    print('Name of Input rule: {}'.format(response_json_firewall_input.get('results')[i]['name']))
                    count_interface = len(response_json_firewall_input.get('results')[i]['source']['src_interface_list'])
                for item in range(count_interface):
                    print('In interfaces {}\t:{}'.format(item,response_json_firewall_input.get('results')[i]['source']['src_interface_list'][item]['name']))
                print('Service List: {}'.format(response_json_firewall_input.get('results')[i]['service_list']))
                print('is_log_enabled: {}'.format(response_json_firewall_input.get('results')[i]['is_log_enabled']))
                print('Description: {}'.format(response_json_firewall_input.get('results')[i]['description']))
                print('Status: {}'.format(response_json_firewall_input.get('results')[i]['status']))
                print('=========================================================')
        return True   
    except Exception as error:
        print(error)
        return False 


url_firewall_input=api_urls['api_firewall_input']

if not Get_firewall_Input(url_firewall_input):
    Get_firewall_Input(url_firewall_input,20)



def Get_site_t0_site(url_site_to_site,input_timeout=10):

    try:
        response_vpn_input = requests.get(url_site_to_site,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=input_timeout)
        response_vpn_input_json = response_vpn_input.json()
        # print(response_vpn_input_json)
        print('count of ipsec Tunnels: \t{}'.format(response_vpn_input_json.get('count')))
        tunnel_count = int(response_vpn_input_json.get('count'))
        for i in range(tunnel_count):
            print(i)
            print('Name of Ipsec tunnel:\t{}'.format(response_vpn_input_json.get('results')[i].get('name')))
            print('Is Enable:\t{}'.format(response_vpn_input_json.get('results')[i].get('is_enabled')))
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
        return True
    except Exception as err:
        return False    
        print(err)    


url_site_to_site=api_urls['api_site_to_site']
if not Get_site_t0_site(url_site_to_site):
    Get_site_t0_site(url_site_to_site,20)


"""
data_interface= {
            "name": "ETH1",
            "error": None,
            "is_used_in_dhcp": False,
            "is_used_in_ha": False,
            "mac": "00:0C:29:6C:4D:D0",
            "name_sort": "eth00000000",
            "description": None,
            "alias": "ETH1",
            "ip_list": [
                {
                    "ip": "192.168.20.164",
                    "mask": "255.255.255.0"
                }
            ],
            "gateway": "192.168.15.1",
            "is_default_gateway": True,
            "is_dhcp_enabled": False,
            "type": "LAN",
            "is_enabled": True,
            "link_type": "Ethernet",
            "pppoe_username": None,
            "pppoe_password": None,
            "mtu": 1500,
            "last_operation": "update",
            "status": "succeeded",
            "qos_status": "disabled",
            "download_bandwidth": None,
            "upload_bandwidth": None,
            "mode": "interface",
            "data": None
        }
url_test='https://192.168.4.164/api/config/interfaces/ETH1'
# print(json.dumps(data_interface))
# url_add_interfaces = 'https://192.168.4.164/api/config/interfaces?offset=0&limit=20&ordering=enable&mode=interface&real=true'
response=requests.put(url_test,data=json.dumps(data_interface),headers=headers, verify=False)
print(response.status_code)
print(response.content)        
"""