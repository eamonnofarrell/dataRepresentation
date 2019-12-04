import requests

#url = 'https://www.gmit.ie'


#response = requests.get(url)

#print(response.status_code)
#print(response.text)

url = 'http://127.0.0.1:5000/cars'
data = {'reg': '12-Mo-222', 'make':'Opel', 'model':'Zafira', 'price': 20000}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())