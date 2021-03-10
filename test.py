import requests

msg1 = {'msg':'Message 1111'}
req = requests.post("http://localhost:5000/facade", json=msg1)

msg2 = {'msg':'Message 2222'}
req = requests.post("http://localhost:5000/facade", json=msg2)

msg3 = {'msg':'Message 3333'}
req = requests.post("http://localhost:5000/facade", json=msg3)


msg = requests.get("http://localhost:5000/facade")
print(msg.text)