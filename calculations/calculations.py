#Eric Wright
#9/18
import math

def circleArea(radius1):
    PI = 3.14159265359   
#1 get a radius
    radius = radius1
#2 compute the area
    radius = float(radius)
    area = radius * radius * PI
#3 display information back
    print("the area of the circle is:", area)

def pythagorasTherom(ap, bp):
    #a^2 + b^2 = c^2
    a = float(ap)
    b = float(bp)
    c = math.sqrt(a+b)
    print("the third side is",c)

def add_numbers(num1p, num2p):
    num1 = num1p
    num2 = num2p
    num3 = int(num1) + int(num2)
    return num3

question1 = input("Would you like to get the area of a circle? ")
if question1 == "yes" or question1=="y" or question1=="sure":
    radiusx = input("What is the radius ")
    circleArea(radiusx)
    varStop = input("End Program")

elif question1 == "no" or question1 == "nope":
    question2 = input("Would you like to get the side of a triangle? ")

else:
    print("Okay bye")
    varStop = input("End Program")

if question2 == "yes" or question2=="y" or question2=="sure":
    ax = input("Enter the first side of the triangle ")
    bx = input("Enter the second side of the triangle ")
    pythagorasTherom(ax, bx)
    varStop = input("End Program")

elif question2 == "no" or question2 == "nope":
    question3 = input("Would you like to add two numbers together? ")

else:
    print("Okay bye")
    varStop = input("End Program")

if question3 =="yes" or question3=="y" or question3=="sure":
    num1x = input("enter a number ")
    num2x = input("enter another number ")
    num4=add_numbers(num1x, num2x)
    print("the sum of your numbers are", num4)
    varStop = input("End Program")

else:
    print("Okay bye")
    varStop = input("End Program")


