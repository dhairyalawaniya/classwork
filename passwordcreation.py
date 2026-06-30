#Ask the user to create a password.
#The password must satisfy these conditions:
#At least 8 characters long.
#Must contain the "@" symbol.
#If the password is invalid, display an appropriate message and ask again.
#Continue until a valid password is entered.
while True :
   a = input("create a valid password: ")
   b = len(a)
   if b >= 8 and "@" in a :
      print ("password created!")
      break
   else :
      print ("password does not match the requirments,\nTry Again")
      
 