import cmath

print ("This Programme Finds roots of second degree equation as ax^2 + bx + c \n")

print ("Please enter a \n ")
a=input()

print ("Please enter b \n")
b=input()
print ("Please enter c \n")
c=input()

delta= b*b - 4*a*c

Root1 = (-b-cmath.sqrt(delta))/(2*a)
Root2 = (-b+cmath.sqrt(delta))/(2*a)

print ("Root 1 : {:.2f}  Root 2 : {:.2f} " .format(Root1 , Root2) )