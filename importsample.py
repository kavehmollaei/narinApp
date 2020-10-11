import json,requests

from os import setxattr
from requests import get
import sys


class User:
    activeUsers = 0

    def __init__(self,name,family):
        
        assert isinstance(name,str)
        self.name=name
        self.family=family
        self.key = ''
        User.activeUsers +=1
       
    def __repr__(self):
        return 'name is {} and family is {}'.format(self.name,self.family)
    @classmethod
    def getActiveUsersCount(User):
        print('active users count is {}: '.format(User.activeUsers))
   
    def Logout(self):
        User.activeUsers -=1
        print('User {} logged out'.format(self.name))
    
    @classmethod
    def from_string(User,string_data):
        n,f = string_data.split(',')
        user0= User(n,f)
        return user0
    @classmethod
    def User_key(User,name,family,key):
        data_key_value = "123!{}@#!@3${}322{}324".format(name,family,key)
        return 'You password is {}'.format(data_key_value)

        
    


User.getActiveUsersCount()
User.User_key('kaveh','mollaei','fjsdlkjfls')

user1 = User('sdsd','mollaei') 
user2 = User('s','dd')
# user1.Logout()
# print(User.from_string('kaveh,mos').name)
print(User.User_key('ffd','fddf','fdf'))

# User.getActiveUsersCount()


# User.getActiveUsersCount()
me = User('kjhg','so')
print(me)

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x,indent=4))

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url,timeout= 5)
response_json= response.json()
print(type(response_json))
f = open('demotest.txt','w')
f.write(str(response_json[0]))
