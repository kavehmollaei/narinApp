curl --insecure  --request POST  https://192.168.4.164/api-token-auth/ -H "Accept: application/json" -H "Content-type: application/json" --data '{"username":"admin","password":"admin"}' --connect-timeout 10 | jq

