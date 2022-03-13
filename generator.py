import requests
import time
while True:
    r = requests.get('https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new')
    number = int(r.text)
    data = {'value': number}
    print(number)
    requests.post('http://localhost:8081/randomInt', json=data)
    time.sleep(0.5)