from github import Github
import base64

g = Github("")

repo = g.get_repo("AsciiKay/Beginners-Python-Examples")

contents = repo.get_contents("math/aircraft_thrust.py")

print(contents.decoded_content.decode("utf-8"))
