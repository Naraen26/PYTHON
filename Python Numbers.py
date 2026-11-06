#INTEGER 
x = 33333
y = -33333
z = 1

print(type(x))
print(type(y))
print(type(z))

#FLOAT 

x = 1.0
y = -222.4444
z = 1.010

print(type(x))
print(type(y))
print(type(z))


#COMPLEX

x = 35 + 5j
y = 5j
z = -5j

print(type(x))
print (type(y))
print(type(z))

#COVERTING THE VALUES FLOAT,COMPLEX, INTEGER 
x = 22
y = 22.4
z = 1j

# CONVERTING A INTO FLOAT
a = float(x)

# CONVERTING B INTO COMPLEX
b = complex(y)

# CONVERTING C INTO INTEGER
c = int(z.real)

print(a)
print(b)
print(c)


#RANDOM NUMBER 
import random
print(random.randrange(1, 10))