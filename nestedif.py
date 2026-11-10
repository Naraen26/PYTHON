
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
    