import json
import re
import camelcase

me = '{"name":"Diallo","id":16,"class":182,"statue":"single","age":21}'
you = json.loads(me)  # To convert form json to python
print(you["name"])

py = {"name": "Alpha oumar ", "Age": 21}
js = json.dumps(py)
print(py["name"], py["Age"])

print(json.dumps(439.34))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print(json.dumps(me, indent=4))

text = "I really like that song it sound nice to me "
print(re.search("^I.*me$", text))
try:
    camel = camelcase.CamelCase()
    print(camel.hump(text))
except AttributeError:
    print("Exception")
finally:
    print("Something is going weong ")
