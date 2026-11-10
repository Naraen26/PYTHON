import json

x = '{"name":"senjuuu", "age":20, "city":"tokyo"}'

y = json.loads(x)

print(y["age"])
print(y["name"])
print(y["city"])

#SAMPLE 2

import json

print(json.dumps({"name": "nagi", "age": 20}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "cherry")))
print(json.dumps("helloOOOWWW"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))