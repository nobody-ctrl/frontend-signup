import requests
r = requests.post('http://localhost:3000/auth/signup', json={"name": "Ana", "email": "jdsgfiu@gmail.com", "password": "jdhfiwjfhie"})
print(r.status_code)
print(r.json())
