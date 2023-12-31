import requests

url = 'https://api.pwnedpasswords.com/range/'+'CBFDAC'

res = requests.get(url)
print(res)