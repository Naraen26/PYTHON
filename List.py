#LIST(USED TO STORE MULTIPLE VALUES IN A SINGLE VARIABLES )

myList=["apple","orange","kiwi","strawberry"]
print (myList)

#Len()

mylist = ["BMW","AUDI","BENZ","SKODA","FORD"]
print(len(mylist))#LEN USED TO FIND HOW MUCH VALUES INSIDE THIS VARIABLE

#ACCESS THE LIST ITEM 


#CAN CHOOSE A SINGLE VAUE WHICH YOU NEED THE VALUES STARTS FROM 0

teamlist = ["mikey","draken","takemichy","mitsuya"]
print (teamlist[1]) 


#CAN CHOOSE A SINGLE VALUE IT STARTS FROM THE END 
teamlist = ["isagi","rin","bachira","chickgiri"]
print (teamlist[-2])

#RANG OF INDEXES
teamlist =["orange","kiwi","apple","strawberry","lemon"]
print(teamlist[2:]) #LEAVING THE FIRST TWO EVERYTHING WILL DISPLAY


teamlist =["orange","kiwi","apple","strawberry","lemon","jackfruit"]
print(teamlist[:4]) #TAKES THE FIRST 4 VALUES


#CHANGE THE LIST VALUE

thisteam=["BMW","AUDI","FORD","HUYNDAI"]
thisteam[3] = "TATA"
print(thisteam)

#SAMPLE2
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#INSERT VALUES

thisteam = ["apple", "banana", "cherry"]
thisteam.insert (2,"orange")
print (thisteam)

#APPEND ITEM
thislist = ["luffy", "zoro", "sanji"]

thislist.append("robin") #ADDS THE VALUE AT THE END

print(thislist)

#REMOVE THE VALUE 

thislist = ['luffy', 'zoro', 'LUFFY','sanji', 'robin']
thislist.remove('luffy') #USED TO REMOVE A  VALUE THAT OCCURANCE MULTIPLE TIMES
print(thislist)


# pop() METHOD USED TO REMOVE SPECFIC VALUE
thislist = ["ash","pikachu","may","brock"]
thislist.pop(0)
print (thislist)


#CLEAR
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)