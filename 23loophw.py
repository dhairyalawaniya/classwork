a = int(input('enter the number'))
b = 0
if a == 0 :
 b = 1
while a>0:
 b += 1
 a = a//10
print (b)