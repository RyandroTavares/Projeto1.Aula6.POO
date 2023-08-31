import requests
import github

respostaAPI = requests.get("https://api.github.com/users/RyandroTavares")
respostajson = respostaAPI.json()

login = respostajson["login"]
idhub = respostajson["id"]
avatar_url = respostajson["avatar_url"]
repos_url = respostajson["repos_url"]
name = respostajson["name"]
location = respostajson["location"]
bio = respostajson["bio"]

github = github.Github()
github.insert(login, idhub, avatar_url, repos_url, name, location, bio)

print(github.get(48698466))