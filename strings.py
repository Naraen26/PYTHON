#STRINGS ("",'')

#("")
print("this is the sample for double quation")
#('')
print('this is the sample for single quation')

#SLICING STRINGS

x = "sample,slicing"
print(x[:6]) #REMOVES THE WORDS FROM THE START

y = "sample, slicing"
print (x[3:]) #REMOVES THE WORDS FROM THE END

#UPPERCASE 
x = "helloww python"
print(x.upper())

#LOWERCASE 
y = "HELLOW PYTHON"
print(y.lower())

#REMOVE WHITESPACE 
a = " Hello, World! "
print(a.strip())


#REPLACE STRING

x = "jelloww python"
print(x.replace("j","h"))

#SPLIT STRING
a = "Hello, World!"
print(a.split(","))

#CONCENTNATION STRING (USED TO ADD SPACE BTW LETTERS)
a = "This is"
b = "mikey"
print(a + " " + b)

#FORMAT STRING
age =25 
txt=(f"my age is {age}") #USING F STRING
print (txt)

price = 45
txt=(f"cost of the biscuit:{price:.2f}")#:.2F IS USED TO MAKE DECIMAL POINT AFTER THE NUMBER
print (txt)