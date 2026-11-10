#ARRAY (BASIC SYNTAX)
 
names = ["Manjiro", "Draken", "Mitsuya", "Senju", "Takemichy"]
print(names)

#LIST ([])

names = ["Manjiro", "Draken", "Mitsuya"]
fruits = ["apple","orange","cherry"]
cars = ["bmw","ford","benz"]

print(names)
print(fruits)
print(cars)

#INDEX 
fruits = ["apple","cherry","grapes","orange"]
print (fruits[2])

#CHANGE THE ELEMENT 

cars = ["bmw", "audi " ,"benz"]
cars[1] = "ford"
print(cars)

#ADD ELEMENT

names = ["isgai","rin","chigri"]
names.append("bachira")
print (names)

#INSERT (CAN DECIDE WHERE WE WANT TO ADD THE VALUES)
fruits =["orange","apple","cherry"]
fruits.insert(2,"jam")
print (fruits)

#REMOVE THE ELEMENT
cars = ["volvo","ford","tata","bmw"]
cars.remove("volvo")
print(cars)

#POP (REMOVE THE VALUE THORUGH INDEX)

cars = ["volvo","ford","tata","bmw"]
cars.pop(3)
print(cars)

#FIND THE LENGTH OF THE LIST 
names = ["mikey","mitsuya","draken","senju","happy","angry","baaji"]
print(len(names))