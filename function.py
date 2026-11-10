def myfunction():
    print("sample program for function")
myfunction()

# SAMPLE 2
def evenodd(x):
    if (x % 2 == 0):
        return "even"
    else:
        return "odd"

print(evenodd(8))
print(evenodd(15))

#ARGUMENTS 
def fav(name):
    print("my fav character in tokyo revengers is:", name)

fav("manjiro")

#SAMPLE 2
def my_function(country = "paris"):
    print("i am from",country)
my_function("austraila")
my_function("norway")
my_function("brazil")
my_function("argentina")

#SAMPLE 3 
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + " name is", name)

my_function(animal = "dog", name = "Buddy")

#SAMPLE 4
def my_function(name, age, breed):
    print("My dog name is:", name)
    print("His age is:", age)
    print("Its breed is:", breed)

my_function(name="mara", age="3", breed="dobberman")


#*ARGS
def my_function(*args):
    print("Type:", type(args))
    print("first name:",args[1])
    print("second name:",args[2])
    print("third name:",args[0])
my_function("isagi","bachira","rin")


# **KWARGS
def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

my_function(name="senju", age=20, city="tokyo")