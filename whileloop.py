#WHILE LOOP

num = 1
while num <=40:
    print(num)
    num +=1

#BREAK STATEMENT

x = 1
while x <= 20:
    if x == 10:
        break
    print(x)
    x +=1

#CONTINUE STATEMENT
i = 1
while i < 10 :
    i+=1
    if i == 5:
        continue
    print(i)

#ELSE STATEMENT
i = 1
while i < 10:
  print(i)
  i += 1
else:
  print("i not lesser than 10")