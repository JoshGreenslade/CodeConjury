import requests

res = requests.get("https://api.github.com/users/octocat")
data = res.json()
print(data)
