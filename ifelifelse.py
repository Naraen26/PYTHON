#IF CONDITION 

a = 20
b = 40
if  a < b:
    print("a is lesser than b") 

#SAMPLE 2

num = 15 
if num  > 0 :
    print("num is positive")

# IF STATEMENT MULTIPLE BLOCK 

age = 20
if age > 18:
    print("you are eligble to drive")
    print ("you are able to vote")
    print("you can aplly for license")


#ELSIF

a = 45
b = 45
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")

#SAMPLE 2

a = 80
if a > 85:
    print("A GRADE")

elif a > 60 & a < 80:
    print("B GRADE")

#SAMPLE 3

age = 16

if age > 60:
    print("you are older")

elif age > 45 and age < 60:
    print("you are moderate age")

elif age < 20:
    print("you are below the age category")

#SAMPLE 4 

day = 7
if day ==1 :
    print("monday")
elif day ==2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday")
elif day == 6:
    print("saturday")
elif day == 7:
    print("sunday")

#ELSE

a = 18
b = 45
if a > b:
    print("a is greater than b ")
elif a == b:
    print("a is equal to b")
else :
    print("b is greater than a")

#SAMPLE 2 
temperature = 17
if temperature > 25:
    print("sunny climate")
elif temperature  > 18 and temperature  < 25 :
    print("moderate climate")
else:
    print("cool climate")


# NESTED IF

score = 55
attendance = 55
ass_submited = True

if score > 70:
    if attendance > 59:
        if ass_submited:
            print("you are the best student")
        else:
            print("you did not submit the assignment")
    else:
        print("your attendance may be low")
        print("FAIL")
else:
    print("your score may be low")
    print("FAIL")

#SAMPLE 2 
user_name = "majirosano"
password = ""
active = True

if user_name:
    if password:
        if active:
            print("login successfully")
        else:
            print("your account is inactive")
    else:
        print("enter a valid password")
        print("login failed")
else:
    print("enter a valid username")
    print("login failed")