
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
    j+=1

print("-----------------------------")

Language=["C","C++","Java","PHP","Javascript","Python"]
print(Language)
print("I am expert in "+Language[2])    # printing what contains index 2
print(Language[2:])      # printing from index 2 to end
print(Language[-1])      # printing from opposite
print("Kotlin" in Language)   # checking 
print(Language + ["Kotlin",27])   # adding more contenet to list
print(Language*3)    # multiplying 

print(len(Language))  # measuring size of List
Language.append("Swift")
print(Language)
Language.insert(3,"C#")   # inserting C# in index 3 no position
Language.remove("PHP")
print(Language)
Language.sort()
Language.reverse()
Subject=Language.copy()
print(Subject)
position=Language.index("Java")
print(position)
counting=Subject.count("Java")
print(counting)

print(" Range function----------------------------------------------------")

num1= list(range(10))    #Print 0 to 9
print(num1)
print(num1[7])     # Print what contains no 7 index
num2=list(range(5,11))  # Print from 5 to 10
print(num2)

num3=list(range(5,101,3))  # print from 5 to 100  and everytime difference is 3 or increament 3
print(num3)

print("--------------------------------------------------------")
num=[10,20,30,40,50,60,70,80,90,100]
print(num)

sum=0
for x in num:
     print(x)
     sum=sum+x
print("Sum of list is ",sum)

print("-Series----------------------------------")

# Series sum 1+2+3+4+5+6......n

n= int(input("Enter the number range:"))
sum =0 

for x in range(1,n+1,1):
       sum=sum+x
print(sum)

#Series sum of even numbers 2+4+6+8+10.....(n+2)
sum1=0
for x in range(2, n+1, 2):
         sum1=sum1+x
print(sum1)

#Series sum of Odd number 5+7+9+11+13+15.....(n+1)

sum2=0
for x in range(5,n+1,2):
         sum2=sum2+x
print(sum2)

# Series of square 1^1 + 2^2 + 3^3 + 4^4 + 5^5 +........n^n

sum3=0
from math import *
for x in range(1,n+1,1):
         sum3=sum3+ pow(x,x)
print(sum3)

# Factorial

m= int(input("Enter Factorial:"))
fact=1
for x in range(1,m+1,1):
         fact=fact*x
print(fact)

# prime number 
p=False # defining a flag variable 
for i in range (2,m,1):
        if(m%i)==0:
            p=True
            break

if p==True:
    print(m," is not a prime number")

else :
    print(m," is a prime number ")

print("GCD LCM---------------------------------")

num1=int(input("Enter 1st number "))
num2=int(input("Enter 2nd number "))

if(num1>num2):
   smaller=num2
else :
   smaller=num1

for i in range(1,smaller+1,1):
         if((num1%i==0) and (num2%i==0)):
             GCD=i

print("GCD is ",GCD)

LCM = (num1*num2)/GCD
print("LCM is ",LCM)'''

print("Pattern-------------...............................")