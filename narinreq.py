import json
import requests

#p = req.post(http://192.168.5.100/config/backup, josn={"description":"test","version":"null","file":"null","datetime":"null"})
"""login_params = dict()
login_params['json'] = {"username": "admin", "password": "admin", "remember": "true"}
login_params['username'] = "admin"
login_params['password'] = "admin"
login_p = req.post("https://192.168.5.210:9090/api-token-auth/", params=login_params, verify=False)
print(login_p.status_code)
print(login_p.content.decode())
params = dict()
params['json'] = {"description":"test"}

p = req.post("https://192.168.5.210:9090/config/backup?client_ip=192.168.5.100", params=params, verify=False)

#p=req.post("http+unix://%2Ftmp%2Fapi.sock/api/entity/addresses?client_ip={}".format(client_ip), json={"name":"${new_name}"})
print(p.status_code)
print(p.content.decode())
"""






def send_and_get_data_from_other_peer(dist_ip, api_addr, method, data, headers={}):
    headers['content-type'] = 'application/json'
    headers['Accept'] = 'application/json'
    url = 'https://' + dist_ip + api_addr
    req = requests.session()
#    req.mount('https://', TLSAdapter())
    import urllib3
    urllib3.disable_warnings()
    if method == 'POST':
        response = req.post(url, data=json.dumps(data), headers=headers, verify=False)
    elif method == 'GET':
        response = req.get(url, data=json.dumps(data), headers=headers, verify=False)
    elif method == 'PUT':
        response = req.put(url, data=json.dumps(data), headers=headers, verify=False)
    elif method == 'DELETE':
        response = req.delete(url, data=json.dumps(data), headers=headers, verify=False)
    else:
        raise Exception('Invalid method')
    return response


def get_token(peer2_address):
    login_data = {'username': 'admin', 'password': 'admin'}
    # login_data = {'username': 'admin', 'password': 'admin'}
    token = send_and_get_data_from_other_peer(peer2_address, '/api-token-auth/', 'POST', login_data)
    if token.status_code == 200:
        return token.json()['token']
    else:
        raise serializers.ValidationError('Authorization failed in High Avalaibility')

ip_address = "192.168.4.164"
token = get_token(ip_address)
headers = {'Authorization': 'Token {}'.format(token)}
print(token)

"""
data = {"description":"test"}
responce = send_and_get_data_from_other_peer(ip_address,
            '/config/backup',
            'POST',
            data,
            headers)
print(responce.status_code)
print(responce.content.decode())
"""