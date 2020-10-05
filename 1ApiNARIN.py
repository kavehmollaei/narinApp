import requests
import json
import urllib3
from urllib3 import disable_warnings
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from arprequest import ArpRequest
import arpreq
#build header
headers={}
headers['content-type'] = 'application/json'
headers['Accept'] = 'application/json'



login_data = {'username': 'admin', 'password': 'admin'}


# send request for get login token
req = requests.post('https://192.168.4.164/api-token-auth/',data=json.dumps(login_data),verify=False,headers=headers)
token=req.content.decode()
token_json=json.loads(token)
# print(token_json)


# add token to the header
headers['Authorization']= f"Token {token_json['token']}"


print(headers)



# get token result you can Un comment this for see token
#print(token_json['token'])



# send request for show interfaces
url_interfaces ='https://192.168.4.164/api/config/interfaces?offset=0&limit=20&ordering=enable&mode=interface&real=true' 
response_show_interface=requests.get(url_interfaces,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=30)
#decode response
response_show=response_show_interface.content.decode()

#see type of response_show
#print(type(response_show))

# count of interfaces
t = json.loads(response_show)
count_of_interfaces = len(t['results'])
print('count_of_interfaces:{}'.format(count_of_interfaces))
# print(t['results'][1])
print('=============')
# print(print(t['results'][0]))
# print(t['results'][0]['ip_list'])
# get interface informations
for i in range(0,count_of_interfaces):
    print('DHCP_STATUS ETH{}----->'.format(i)+ str(t['results'][i]['is_dhcp_enabled']))
    print('IP_LIST_ETH{}----->'.format(i)+str(t['results'][i]['real_ip_list']))
    print('ETH{} was ---->'.format(i)+t['results'][i]['status'])
    print('LINK_TYPE ETH{}----->'.format(i)+str(t['results'][i]['link_type']))
    print('TYPE WAN OR LAN ETH{}----->'.format(i)+str(t['results'][i]['type']))
    print('Default Gateway is :----->',str(t['results'][i]['gateway']))

    print('==============================================================')
url_route = 'https://192.168.4.164/api/config/static_routes?offset=0&limit=10&ordering=name&real=true'
response_show_routeing_table=requests.get(url_route,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=30)
result_route=response_show_routeing_table.content.decode()


print(type(result_route))
result_route_json=json.loads(result_route)



# print(result_route_json)
print(result_route_json['count'])
route_count=result_route_json['count']
for i in range(0,route_count):
    print('Name : {}'.format(result_route_json['results'][i]['name']))
    print('Destination_Ip : {}'.format(result_route_json['results'][i]['destination_ip']))
    print('Destination_Mask: {}'.format(result_route_json['results'][i]['destination_mask']))
    print('Gateway: {}'.format(result_route_json['results'][i]['gateway']))
    print('Name of Interface: {}'.format(result_route_json['results'][i]['interface']['name']))
    print('Description: {}'.format(result_route_json['results'][i]['description']))
    print('========================================================================================')

# route_os = os.system('route -n')
# print(route_os)


# Get version
url_version='https://192.168.4.164/api/version'
response_show_version = requests.get(url_version,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=30)
response_show_version=response_show_version.content.decode()
response_show_versio_json=json.loads(response_show_version)
print('version of device: {}'.format(response_show_versio_json['version']))

#Get hostname
url_hostname='https://192.168.4.164/api/config/settings/host-name'
Response_Show_Hostname = requests.get(url_hostname,headers={'Authorization': 'Token '+token_json['token']},verify=False,timeout=30)
Response_Show_Hostname= Response_Show_Hostname.content.decode()
Response_Show_Hostname_json=json.loads(Response_Show_Hostname)
print('Hostname: {}'.format(Response_Show_Hostname_json['data']['value']))
print('===================================================')
# ar = ArpRequest('192.168.50.1', 'enp0s25')
# print(ar.request)
print(arpreq.arpreq('192.168.50.1'))


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