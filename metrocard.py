#Name:Zaiba Iqbal
#Date: October 13, 2017
#This program prints Metrocard prices

mess=int(input("How often do you plan to ride the bus or subway this week?"))
x=mess
y=x*2.48
z=31.0/x
if x==1 or x==2:
    print("You should buy a regular ticket.")
elif x>=3 and y<31:
    print("You should buy a regular ticket.")
else:
    print("You should buy a 7-day ticket.")
