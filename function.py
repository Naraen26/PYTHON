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