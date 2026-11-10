#FOR LOOP(BASIC SYNTAX)
 
names = ["manjiro sano","draken","senju"]
for x in names:
    print(x)

#BREAK STATEMENT
fruits = ["cherry","apple","banana"]
for x in fruits:
    print (x)
    if x == "apple":
          break
    

#CONTINUE STATEMENT
names = ["manjiro sano", "draken", "takemichy", "senju", "mitsuya"]

for x in names:
    if x == "takemichy":
        continue
    print(x)

#RANGE(STOP)

for x in range(10):
  print(x)

#RANGE(START/STOP)

for x in range(2,5):
    print(x)

#RANGE(START,STOP,STEP) //INCREMENT BY THE SPECIFIED STEP VALUE

for x in range (3,30,3):
    print(x)