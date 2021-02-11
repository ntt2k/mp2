import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp1'

payload = {
		'ip_address1':'34.207.67.255:80',
		'ip_address2':'3.93.172.163:80',
		'load_balancer':'lb-ec2-docker-fastapi-2099620855.us-east-1.elb.amazonaws.com:80',
		'submitterEmail':'trungtn2@illinois.edu',
		'secret':'Rc30DsdRYkNe5Q4l'
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
