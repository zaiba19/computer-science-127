#Name:Zaiba Iqbal
#Date:October 6,2017
#This program prints a turtle string

import turtle 
tim = turtle.Turtle()
myWin = turtle.Screen()     
commands = input("Please enter a command string: ")
for ch in commands:
    if ch == 'F':            
        tim.forward(50)
    elif ch == 'L':          
        tim.left(90)
    elif ch == 'R':          
        tim.right(90)
    elif ch == '^': 
        tim.penup()
    elif ch == 'v':          
        tim.pendown()
    elif ch == 'B':            
        tim.backward(50)
    elif ch == 'r':          
        tim.color("red")
    elif ch == 'g':          
        tim.color("green")
    elif ch == 'b':          
        tim.color("blue")
    else:                    
        print("Error: do not know the command:")
print("See graphics window for your image")
myWin.exitonclick()
