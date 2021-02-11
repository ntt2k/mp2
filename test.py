import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp1'

payload = {
		'ip_address1':  '34.207.67.255:80',
		'ip_address2':  '3.93.172.163:80',
		'load_balancer' :  'ec2-docker-fastapi-933855433.us-east-1.elb.amazonaws.com',
		'submitterEmail':  'trungtn2@illinois.edu',
		'secret':  'Yfvz3v3N2I1usFOL'
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
