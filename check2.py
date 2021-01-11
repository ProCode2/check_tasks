import os
import sys
import base64
from dotenv import load_dotenv
from github import Github

# get current working directory
cwd = os.getcwd()


# set env vars
load_dotenv()

token = os.getenv("TOKEN")

users = ['asharathore/coding-practise', 'Aayushi-Mittal/Rock-Paper-Scissors']
g = Github(token)


for user in users:
    repo = g.get_repo(user)
    filename = user[:5]
    try:
        contents = repo.get_contents("index.html")
        with open(f'{cwd}/{filename}.html', 'w+') as f:
            f.write(contents.decoded_content.decode('utf-8'))
    except TypeError as e:
        print(e)
    except:
        print("No such file found")



