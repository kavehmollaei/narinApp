import requests
import json
req = requests.get('https://192.168.4.164/api/config/interfaces?offset=0&limit=20&ordering=enable&mode=interface&real=true',headers={'Authorization':'Token 5928caeef79252f746fddd459c2af97b8c8f9fe5'},verify=False)
# print(req.headers)

# print('+++++++++++++++++++++')
# print(req.content)

con = req.content
print(json.loads(con)['results'][0]['real_ip_list'])
print(json.loads(con)['results'][1]['real_ip_list'])