import requests
import json
import os
from dotenv import load_dotenv
      
load_dotenv()

# Getting the username and token from .env file
username = os.getenv("USERNAME")
token = os.getenv("TOKEN")
      
repos_url = f"https://api.github.com/users/{username}/repos"
# init a session with requests
gh_session = requests.Session()
# enable authontication
gh_session.auth = (username, token)
# parsing to JSON and getting the repos
repos = json.loads(gh_session.get(repos_url).text)

# printting the repos names and their ids
for repo in repos:
  print(repo["id"], repo["name"])
