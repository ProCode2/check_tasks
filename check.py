
from github import Github
import base64

g = Github("")

repo = g.get_repo("ProCode2/CSES_Problmes")

contents = repo.get_contents("")

while contents:
    file_content = contents.pop()
    if file_content.type == 'dir':
        contents.extend(repo.get_contents(file_content.path))
    else:
        print(file_content.decoded_content)

