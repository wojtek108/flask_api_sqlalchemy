import requests

BASE = 'http://127.0.0.1:5000/'

#response = requests.get(BASE + 'data')
#response = requests.get(BASE + 'data/vetim')
response = requests.get(BASE + 'data')

#response = requests.post(BASE + 'data/wg')
#response = requests.post(BASE + 'data')





print(response)
print(response.json())

