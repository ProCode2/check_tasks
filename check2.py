from github import Github
import base64

g = Github("5ceb82968b58c4c053f404323156de3eea91db5f")

repo = g.get_repo("AsciiKay/Beginners-Python-Examples")

contents = repo.get_contents("math/aircraft_thrust.py")

print(contents.decoded_content.decode("utf-8"))
