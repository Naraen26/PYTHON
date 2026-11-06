#BOOLEAN

marks = 50
if marks >= 75:
    print("YOU ARE A GRADE")

elif marks <= 60:
    print("YOU ARE FAIL")

else:
    print("YOU ARE BELOW A GRADE")

#SAMPLE2

cart_items = []

if cart_items: 
    print("Proceed to checkout.")
else:
    print("Your cart is empty.")


#SAMPLE3 

a = 50
b = 40
c = 32

if a > b and a > c:
    print("A IS GREATER THAN B AND C")

elif b > c:
    print("B IS GREATER THAN C")

else:
    print("VALUE DOES NOT EXIST")

#BOOLEAN OPERATOR

#OR OPERATOR

a = 10
b = 20
c = 15

if a > b or c < b : #ATLEAST ONE SHOULD BE TRUE 
    print ("true")
else:
    print("condition are false")

#AND OPERATOR 

a = 10
b = 20

if a > 5 and b > 15:
    print("BOTH CONDITIONS ARE TRUE")
else:
    print("CONDITION IS FALSE")

#EQUALITY OPERATOR (==)
password = 1234

if password == 1234:
    print("LOGIN SUCCESSFUL")
else:
    print("WRONG PASSWORD")

#(!=)
password != 1234

if password == 1234:
    print("WRONG PASSWORD")
else:
    print("LOGIN SUCCESSFUL")