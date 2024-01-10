num1=float(input("first no."))
num2=float(input("second no."))
print("for * press 1\nfor / press 2\nfor + press 3\nfor - press 4")
preference=int(input("enter your preference1-4:"))
if preference==1:
 print(num1*num2)
elif preference==2:
  print(num1/num2)
elif preference==3:
  print(num1+num2)
elif preference==4:
  print(num1-num2)
else:
 print("invalid")
