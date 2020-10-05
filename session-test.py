import requests
import json
import urllib3
from urllib3 import disable_warnings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers={}
headers['content-type'] = 'application/json'
headers['Accept'] = 'application/json'

url = 'https://formulae.brew.sh/api/formula.json'
urll='http://api.plos.org/search?q=title:"Drosophila" AND body:"RNA"&fl=id&start=100&rows=100'
urlll='https://dl7.serverdl.host/user/ali/Movie/1399/06/Honest.Candidate.2020.1080p.WEB-DL.x264.YTS-SalamDL.mkv'
google='https://www.gmail.com'


#######################################################################################
headers={}
headers['content-type'] = 'application/json'
headers['Accept'] = 'application/json'



login_data = {'username': 'admin', 'password': 'admin'}



mysession=requests.session()
response=mysession.post('https://192.168.4.164/api-token-auth/',data=json.dumps(login_data),verify=False,headers=headers)
print(response.json())

token_json=response.json()

print(token_json)
mysession.headers.update({"Authorization":f"Token {token_json['token']}"})
res_p=mysession.get('https://192.168.4.164/api/entity/addresses?offset=0&limit=10&ordering=name',verify=False)
print(res_p.json())