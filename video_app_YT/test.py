import requests

BASE = 'http://127.0.0.1:5000/'

#response = requests.get(BASE +'helloworld/tim')
#response = requests.get(BASE +'helloworld/bill')
#response = requests.post(BASE +'helloworld')

data = [ 
        {'name': 'jakis tytul', 'views': 4500, "likes": 10},
        {'name': 'jakis tytul 2', 'views': 8500, "likes": 1110},
        {'name': 'jakis tytul 3', 'views': 4500, "likes": 78910}
        ]

for i in range(len(data)):
    response = requests.put(BASE +'video/' + str(i+i), data[i])
    print(response.json()) 
    print(response)
    
input()
#response = requests.delete(BASE +'video/0')
#print(response)
response = requests.get(BASE +'video/8')
