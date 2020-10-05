import os
from logging.handlers import RotatingFileHandler
import json,time,platform,subprocess,logging,requests,urllib3
from urllib3 import disable_warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# logging.basicConfig(format='%(asctime)s:>>>>%(message)s',level=logging.DEBUG ,filename='log-test.log',filemode='a')


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
