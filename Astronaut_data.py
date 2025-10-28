import json
import urllib.request
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)# result = json.loads(response.read())
result = json.loads(response.read())
print("People in space: ", result['number'])

people = result['people']
print(people)

for person in people:
  print("Astronaut: "+ person['name']+'\n'+ 'craft: '+ person['craft'])