#VARIABLES
x = "mikey"
y = 25
print (x)
print(y)

#MANY VALUES TO MULTIPLE VARIABLES

#SAMPLE1 

x,y,z = "BMW", "AUDI" , "BENZ"
print (x)
print (y)
print(z)

#SAMPLE2 
fruits = "orange" , "strawberry" , "apple"
x,y,z =fruits
print(x)
print(y)
print(z)


#OUTPUT VARIABLES:

#SAMPLE1
x = "today"
y = "is"
z = "friday"
print(x,y,z)

#SAMPLE2
x = 10
y = 20
print(x +y)

#GLOBAL VARIABLES 
#SAMPLE1
x ="friday"
def myfunction():
    print ("today is "+x)

myfunction()
    
# SAMPLE2
x = "best one"

def myfunction():
    x = "awesome"
    print("today is the " + x)

myfunction()

print("today is " + x)


#SAMPLE3 
def myfunction():
    global x
    x = "the one"

myfunction()

print("surya " + x)