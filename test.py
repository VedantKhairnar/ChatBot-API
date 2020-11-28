import requests
res = requests.get('https://ds-chatbot-api.herokuapp.com/', params={"key": "Hello"})
print(res.text)