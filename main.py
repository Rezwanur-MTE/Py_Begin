
name=input("Enter His name :")
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
print("Sum is",sum)
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

print("List-----------------------------")

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

print("Series------------------------------------")

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
# from math import *
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
print("LCM is ",LCM)

print("Pattern-------------...............................")

x=int(input("Input the line number: "))
for i in range(1,x+1,1):
        print(i*"* ")

for i in range(1,x+1,1):
        print((2*i-1)*"* ")    # everyline has extra 2 star

print("Guessing Game--------------------------------------")    

from random import *

for i in range(1,4):                   # it will test 3 times
    guess=int(input("Guess a number between 1 to 10: "))
    randnum= randint(1,10)
    if randnum==guess :
        print(" It Matches. You won brother")
    else : 
         print("You Lose! try again")
         print("The number was",randnum)

print("User Input in List-----------------------------------") 

n = input("Enter your numbers: ")

list=n.split(",")   # Example of split function
print(list)     

sum=0
for num in list:
    sum= sum + int(num)
print("Sum from User Input list is ", sum)

print("Matrix---------------------------------------------")

matrix=[[4,9,3],
        [0,7,8]]

print("In 0 no row and 2 no column number is ", matrix[0][2])

for row in matrix:
    for column in row:
        print("The matrix holding ",column)

print("Dictionary---------------------------------------")

studentID= {
           "1808059" : "Rezwanur",
           "1808034" : "Jaoyad",
           "1808036" : "Saad",
           "1808044" : "Sagar"
           }
print(studentID["1808059"])
print(studentID.get("1808044","Data not found"))
print(studentID.get("1808045","Data not found"))

print("Tuples---------------------------------------")
students=(  ("Rezwanur",1808059,3), 
            "Jaoyad",
            "Ariful",
            "Anisul",
            "Mitin"
          )

print("Info in 0 no index of Tuples is ", students[0])
print("Data from 1 no index to end are", students[1:])

print("Set-------------------------------------------")

num1={1,2,3,4,5,4,4,5}
print("num1 set contains ",num1)

num2=set([4,5,6,9,1])    # convertig list into set
print("num2 set contains ",num2)

num2.add(7)
num2.remove(6)
print("num2 modified ",num2)

print("Union of Set num1 and num2", num1 | num2)
print("Intersection of set num1 and num2", num1 & num2)
print("Difference of set num1 and num2", num1-num2)

print("Stack and Queue--------------------------------------")

books=[]
books.append("Learn C")
books.append("Learn Java")
books.append("Learn C++")
books.append("python")
books.append("Learn DSA")
books.append("Software Development")

print("The stack of books contains ",books)
books.pop()    # delete one iteam from the last 
print("Mandatories are ",books)

print("Now the top book is ",books[-1])
books.pop()
if not books:
    print("No books left")

from collections import deque

bank= deque(["Anisula","Fahim","Karim","Jaoyad"])
print("People in queue ",bank)
bank.popleft()
print("People who left ",bank)

print("FUNCTION-----------------------------------------____________________________")

def Calculation(x,y,z):
    sum= float(x) + float(y) + float(z)
    print("Sum from the function is ", sum)
    sub= float(z) - float(x)
    print("Subtraction of z and x is ",sub)
    mul= float(x)*float(y)*float(z)
    print("Multiplication of x y z is ",mul)
    div= x/y
    print("Division is ",div)

Calculation(5.3,7.6,9)

def remainder(p,q):
    m=p%q
    return m

result=remainder(9,4)
print("Remainder  of 9/4 is ",result)

def larger(g,h):
    if g>h:
        return g
    else:
        return h

print("Larger number between 49 and 69 is ",larger(49,69))

print("xargs-----------------------------------------------")

def student(*details):
    print(details)

student(1808059,"Rezwanur")
student(1808034,"Jaoyad",3.9)

print("________________________________________________________")

def add(*numbers):
    sum=0
    for num in numbers:
        sum+=num
    print("Sum in example xargs: ",sum)

add(10,20)
add(50,60,70)

print("Lambda function________________________________________________")

# (lambda parameter : expression)(argument pass)

print("Calculating from Lambda function= ",(lambda a,b: a*a + 2*a*b + b*b)(5,7))

print(" \n")

print("Map and filter function ----------------------------------------------")

def square(x):
    return x*x

num=[1,2,3,4,5]
result= list(map(square, num))
print("Square of every number of list using map : ",result)
print("\nfilter ")
print("By Lambda function.....")
result1 = list(filter(lambda x: x%2==0,num))
print("Filtering prime number from list :",result1)

print("Alternatingly by named function.....")

def prime(x):
    return x%2==0

result2=list(filter(prime,num))
print("Filtering prime number from list: ",result2)

print("List comprehenion.....")

num2=[3,5,7,11,13]

result3=[x*x for x in num2]
print("Square operation of num2 list: ",result3)

num3=[4,8,11,9,18,26,31,39]
result4 = [x for x in num3 if x%2==0]
print("Even numbers are ",result4)

roll=[1808059, 1808034,1808044,1808036]
name=["Rezwanur","Jaoyad","Sagar","Saad"]
info= list(zip(roll,name))
print("Merging roll and name list ",info)

print("Recursion------------------------")

def fact(n):
    if n==1:
       return 1
    else:
       return n*fact(n-1)

print("Factorial of given value ",fact(6))

print("Python file----------------------------------------")

file1 = open("researchtopic.txt","r")   #Here file1 is a random variable token, "r" mean readable."w " mean writeable."r+" means readable writeable both
print(file1.readable())

text = file1.read()
print("Text from the file ",text)
size=len(text)
print(size)

file1 = open("researchtopic.txt","r")    
textlist = file1.readlines()              #converting lines into list 
print(textlist)

print("Printing flie by using for loop-----")
file2 = open("researchtopic.txt","r+")
for line in file2:
     print(line)

# writing only "w" will delete previous text from file and let you write new texts
# in appeand mode, "a" - will keep previous text in file and can add new text

file3 = open("LearningPlan.txt","a")
file3.write("\n Learning for research purpose:"
            "\n 1. Excel with Python"
            "\n 2. DSA with Python"
            "\n 3. Statistics with Python"
            "\n 4. Data visualisation"
            "\n 5. ML and DL "
            "\n 6. Solidity and Blockchain")

print("Making a new file and writing text in it through coding ---------------")

file4 = open("About Me.txt","w")
file4.write(" This is Rezewanur Rahman \n Not a nerd but hard worker "
              "\nHSC gpa 4.83 and University GPA 3.18 till 2021\n Studying Mechatronics Engineering\n"
              "Have experience in Microcontroller, Android Development, Game Development \n"
              "Started ML and DL in 2022 for Researching in Market Intelligence "
              "\n My best quality is 'I take the challenge and I try' .")
file5 = open("Web Form.html","w")   # careful , comment the whole thing if you don't want to change web form file.
file5.write("<html>"
"<head> <title> Web Registration form </title>  </head>"
"\n<body>"
"\n<h4> Enter your Information </h4>"
"\n<form>"
"\n<lable>Full Name: </lable>"
"\n<input type="#text"> <br><br>"
"\n<lable> Password: </lable>"
"\n<input type="#password"> <br><br>"
"\n<lable> Email: </lable>"
"\n<input type="#email">"
"\n<br><br>"
"\n<lable> Gender: </lable>"
"\n<input type="#radio">Male"
"\n<input type="#radio">Female"
"\n<input type="#radio">others <br><br>"
"\nReligion: <input type="#checkbox">ISLAM .<input type="checkbox">HINDU. <br><br>"
"\n<lable> Subject: </lable>"
"\n<select>"
"\n<option>Bangla</option>"
"\n<option>English</option>"
"\n<option>Math</option>"
"\n<option>Physics</option>"
"\n<option>Chemistery</option>"
"\n<option>Biology</option>"
"\n<option>ICT</option>"
"\n</select> "
"\n<br><br>"
"\nComment: <br><textarea column="#10" row="5"></textarea> <br>"
"\n<input type="#submit"> <input type="#reset">"
"\n</form>"
"\n</body>"
"\n</html>"

)              # Ha..Ha.. Some text in here are commented out for syntax overlap between Python and HTML

file1.close()

print("____________------------Exception Handling-------------_____________________")

try:
    list=[20,0,30]
    p=int(input("Enter what index you want = "))
    div=list[0]/list[p]
    print("The division between index 0 and ",p," is ",div)
    print("Done with no exception")
except ZeroDivisionError :
       print("Dividing by 0 is not possible you stupid!")
except IndexError:
       print("You are out of index")

finally: 
    print("Whatever runtime error come out I don't care, I will be printed")


def voter(age):
    if age< 18:
        raise ValueError(" You are Invalid Voter.")

    return "You are allowed to vote sir."

try : 

    n=int(input("What's your age? : "))
    print(voter(n))

except ValueError as e :
      print(e)

print("Object Oriented Programming---------------------------------------------------------")
print("Class, constructor and Object --------------------------------------")

class Student:
      name=" "
      roll=" "
      gpa=" "

      def setvalue(self,name,roll,gpa):
          self.name=name
          self.roll=roll
          self.gpa=gpa

      def display(self):
          print("Student's name is ",self.name," Roll is ",self.roll," His GPA is ",self.gpa)

A_Rahim=Student()      # An object of student class
print(isinstance(A_Rahim,Student))
#print(isinstance(Karim,Student))    it will show false cause it is not object of student class
A_Rahim.name="Abdur Rahim"
A_Rahim.roll=1809001
A_Rahim.gpa=3.9

print("Student's name is ",A_Rahim.name," Roll is ",A_Rahim.roll," His GPA is ",A_Rahim.gpa)

Jaoyad=Student()       # Another Object of student class
Jaoyad.name="S M Jaoyad Dipto"
Jaoyad.roll=1808059
Jaoyad.gpa=4
print(f"Name is {Jaoyad.name}, Roll is {Jaoyad.roll}, His CGPA is {Jaoyad.gpa} ")

Fahim=Student()
Fahim.setvalue("Rezwanur Rahman",1808059,3.4)    # passing value in class through function
Fahim.display()        # Accessing function in student Class

from math import *
class EqnSolve:
    a=" "
    b=" "
    c=" "
    def __init__(self,a,b,c):    # it is a constructor , it can receive value from Object.
        self.a=a
        self.b=b
        self.c=c
     
    def determinant(self):      # it is parameterless function , but it will access predefined variables in this class by using 'self' keyword
        p=self.a       # i declared extra p, q, r variables so that it can help writing equation , otherwise i needed to write ' .self ' keyword everytime
        q=self.b
        r=self.c
        x= (-q + sqrt(q*q-4*p*r))/2*p
        print("Solution of the quadratic equation= ",x)


# making object of EqnSolve class 
Calculation1=EqnSolve(5,25,3)   # setting value through constructor during Object declaration
Calculation1.determinant()

class Triangle:
      def __init__(self, base, height):
          self.base=base
          self.height=height

      def calculate_area(self):
          area=0.5*self.base*self.height
          print("Area of the triangle is ",area)

t1=Triangle(15,18)    # t1 is an object of Triangle class
t1.calculate_area()

t2=Triangle(20,30)
t2.calculate_area()

print("Inheritence-------------------------------------")

class Phone:
      def call(self):
          print("You are calling")

      def massege(self):
          print("You are massegeing")

class samsung(Phone):
    # call() and massege() is invisiblly present here
      def camera(self):
          print("You can take photos")

Galaxy_note10= samsung()
Galaxy_note10.call()         # notice here , function in Phone class can be access through object of samsung class
Galaxy_note10.massege()
Galaxy_note10.camera() 

print("Method overriding------------------------------")

class Person:
      name=" "
      age=" "
      def displayfunction(self):
          print(" This guy's name is ",self.name," and he is ",self.age," years old.")

class Teacher(Person):
      qualification=" "
      def displayfunction(self):                # this is same named function of Person class and Teacher class 
          super().displayfunction()
          print(" This person is a teacher, he has a degree on ",self.qualification)

Palash = Teacher()
Palash.name="Palash Kumar Dey"
Palash.age=45
Palash.qualification="Physics"
Palash.displayfunction()

print("Example----------------------------------------")

class Shape:
      def __init__(self,dim1 ,dim2,h ):       # constructor for passing value through object declaration
          self.dim1=dim1
          self.dim2=dim2
          self.h=h
 
      def area(self):
         print("This is Area, Function from shape class")

class Trapisium(Shape):
      def area(self):       # this is overridden
          area=0.5*(self.dim1 + self.dim2)*self.h
          print(" The area of Trapizium is ", area)

class Rectangle(Shape):
      def area(self):      # overridden function from shape class
          area=self.dim1*self.dim2
          print("The area of a rectangle inside the trapizium is  ",area)

a=int(input("Input Dimension 1 = "))
b=int(input("Input dimension 2 ="))
x=int(input(" Input distance between parallel arms= "))

trap1= Trapisium(a,b,x)
trap1.area()

Rec1= Rectangle(a,b,x)
Rec1.area()


print("Multi-level Inheritance---------------------------")

class A:
      def display1(self):
          print("This is inside A class")

class B(A):
      def display2(self):
          print("This is inside B class")

class C(B):
      def display3(self):
          super().display2()
          super().display1()
          print("This is inside C class")

ob1= C()
ob1.display3()

print("Multiple Inheritance---------------------------")
class P:
      def display(self):
          print("This is inside P class")

class Q:
      def display(self):
          print("Printing from Q class")

class R(Q,P):
      pass               # if we want to keep this class empty then we must write 'pass' , otherwise it shows error

Ob2= R()
Ob2.display()



print("Abstraction------------------------------------------------------------")

from abc import ABC,abstractmethod

class Shape:
      def __init__(self, a, b):
          self.a=a
          self.b=b
     
      @abstractmethod
      def area(self):         # Abstract function , which has no body 
          pass

class Triangle(Shape):

      def area(self):          # Must have to use this function cause it is abstracted in Shape class which is inherited here     
          area=0.5*self.a*self.b
          print("Area from Abstraction example ",area)

trivuz= Triangle(5,7)
trivuz.area()



print("Polymorphism ----------------------------------------------------")
     
#Built in polymorphic function 
print(len("Rezwanur Rahman"))
print(len([10,20,30]))

#User define polymorphism

def add(x,y,z=0):
    return x+y+z

print(add(5,7))
print(add(5,7,9))

print("Module---------------------------------------------")

from Area_module import *

Triangle(10,20)
Circle(7)

print("Regular Expression-------------------------------------------------------------\n")

import re

pattern1= r"Colour"

if re.match(pattern1,"Colour of rose is red, What the hell! Your dog is Dead?"):
    print("Matches the pattern at the begining of the string \n")

else:
     print("Pattern doesn't match. \n")

pattern2= r"colour"

if re.search(pattern2,"Black is not a colour, it is absence of light"):
    print("Found a match somewhere in the string \n")

else:
     print("Found nothing. \n")


pattern3= r"love"

print(re.findall(pattern3,"I loved a girl but she lied, I found no existance of love, but D.Brand said love is the one thing we are capable of perceiving that transcends dimensions of time and space, love is powerful , observable"))

pattern4= r"book"
text= " knowledge that we gain from books, but what will you do with just bookish knowledeg unless you can implement that!"

object=re.search(pattern4,text)

if object:
   print(object.start())
   print(object.end())
   print(object.span())

pattern5=r"colour"
text2="My favourite colour is Black, but black is not actually colour it is absence of light"
object2=re.sub(pattern5,"replaced_color",text2)
print("After replace: ",object2)

#this is the end of basic Python
