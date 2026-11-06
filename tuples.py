#TUPLES 

thistuple = ("zoro","luffy","sanji")
print(thistuple)

#TUPLE LENGTH
thistuple = ("zoro","luffy","sanji","chopper") 
print (len(thistuple)) #TELLS HOW MUCH VALUES ARE THERE IN


#ACCESS THE TUPLE ITEM 

thistuple = ("zoro","luffy","sanji","chopper") 
print(thistuple[1])#CAN CALL THE SPECIFIC VALUE THAT WE NEED


#NEGATIVE INDEXING
thistuple = ("zoro","luffy","sanji")
print(thistuple[-1]) #CALLS THE VALUE FROM THE END 


#RANGE OF INDEX
thistuple = ("zoro","luffy","sanji","chopper","ace","goldrogger","whitebeard")
print(thistuple[2:5]) 

#  SAMPLE 2
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #DISPLAYS THE FIRST 4 VALUES

#SAMPLE 3
thistuple =("zoro","luffy","robin","sanji","ace")
print(thistuple[2:])#DISPLAY THE NEXT VALUE AFTER 2

#RANGE NEGATIVE INDEX
 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


#UPDATE TUPLES(IT CANNOT BE CHANGED IT IS IMMUATABLE BUT WE CAN CONVERT IT INTO LIST AND WE CAN CHANGE)]
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y[2]= "dragin fruit"
thistuple = tuple(y)
print(thistuple)

#ADD ITEMS
x = ("apple","banana","cherry")
y = list(x)
y.append ("kiwi")
x = tuple(y)
print (x)

#SAMPLE2
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
x = ("kiwi",)
thistuple += y
thistuple +=x #WE CAN ADD TUPLE TO TUPLE BY THIS METHOD 

print(thistuple)

#REMOVE VALUES

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)