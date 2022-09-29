
'''name=input("Enter His name :")
age=int(input(" the age :"))
gpa=float(input("PUT CG :"))

print(" Programmer's name is "+name)
print("His age is ",age)
print("CGPA ",gpa)
sum=age+gpa
print("Sum of age and GPA is ",sum)

from math import *

result= max(30,50,25)
result2=min(20,90)
result3=abs(-7)
result4= sqrt(49)
result5=pow(2,8)
result6=round(69.9675564)

print(result, "  ", result2," ",result3," ",result4," ",result5," ",result6)

## data type check
num = 20.5
print(type(num))
print(type(True))
## printing in same line
print("I am Rezwanur",end=",  ")
print("my id is 1808059")
##Relational Operator
result7= 30<20
print(result7)

##Control Statement :
mark= int(input("Put your marks: "))
if mark<=33:
    print("You are failed")
if mark>=33:
    print("Congratulation Dude, You passed")
if mark%2==0:
    print("Your mark is even")
else :
    print("Your mark is Odd")

## use of elif

if mark>=80:
    print("You Got A+")
elif mark>=70:
    print("You Got A")
elif mark>=60:
    print("You Got A-")
elif mark>=50:
    print("You Got B")
else:
    print("I am sorry for you, no Grade achieved")



##Nested if
if 7>3:  ## if this condition is true then go to nest line
    if 7>8:
        print("Hey Hi")
    else:
        print("What up boy?")
num1=20
num2=30
num3=40
if num1>num2:
    if num1>num3:
        print("number 1 is bigger")
    else:
        print("number 3 is bigger")
if num2>num1:
    if num2>num3:
        print("Number 2 bigger")
    else :
        print("Number 3 bigger ")

## logical operator && , ||

num4=73
if num4>=80 and num4<=100:      ## if one condition is false then doesnt give output
    print("80 to 100 is A+ Range")
if 70<=num4<=80:
    print("70 to 80 is A range")     ## Python can use this too

print("------------------------------------------------------------")
print("AssalamuAlaykum")

z= int(input("Put your number range"))    # 1+2+3+4......n
i=1
sum= 0
while int(i)<=z:
    print(i)
    sum = int(sum)+ int(i)   #type casted , from string to integer
    i+=1
print("End of counting")
print"Sum is",sum
print("-------------------------------------------------------------") 

# Break and continue

i=1
j=1
while i<=100:
    if i==20:
        break  # break example
    print(i)
    i+=1
print("------- -------")
while j<=100:
    if j==30:
        continue
    print(j)
    j+=1'''

print("-----------------------------")

Language=["C","C++","Java","PHP","Javascript","Python"]
print(Language)
print("I am expert in "+Language[2])    # printing what contains index 2
print(Language[2:])      # printing from index 2 to end
print(Language[-1])      # printing from opposite
print("Kotlin" in Language)   # checking 
print(Language + ["Kotlin",27])   # adding more contenet to list
print(Language*3)    # multiplying 