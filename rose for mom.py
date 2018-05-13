#python画玫瑰花系列
'''
#第一个是最喜欢的平面玫瑰花

# -*- coding: cp936 -*-
for i  in range(1):
    def paint(ang,r,ang2):
        turtle.penup()
        turtle.setheading(ang)
        turtle.pendown()
        turtle.circle(r,ang2)
        
        


    import turtle
    turtle.speed(10)
    turtle.color("white")
    turtle.pensize(6)
    turtle.penup()
    turtle.goto(50,-50)
    turtle.pendown()
    turtle.dot(200,"pink")
    turtle.penup()
    turtle.goto(50,86.6)
    ang = -150
    r = 300
    ang2 =46
    

   
    for i in range(21):

        paint(ang,r,ang2)
        ang2 -= 25
        paint(ang+ang2+25,r,-ang2)
        ang2+=25
        ang+=66
        r=r*0.9


    turtle.penup()
    turtle.goto(-200,-250)
    turtle.color("pink")
    turtle.hideturtle()
    turtle.write("rose for mom", font=('Arial', 40, 'normal'))
        
'''   


#这个是用3D图像画出来的，要求装了numpy,matplotlib

'''
from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm

from matplotlib.ticker import LinearLocator

import matplotlib.pyplot as plt

import numpy as np

fig=plt.figure()

ax=fig.gca(projection='3d')

[x,t]=np.meshgrid(np.array(range(25))/24.0,np.arange(0,575.5,0.5)/575*17*np.pi-2*np.pi)

p=(np.pi/2)*np.exp(-t/(8*np.pi))

u=1-(1-np.mod(3.6*t,2*np.pi)/np.pi)**4/2

y=2*(x**2-x)**2*np.sin(p)

r=u*(x*np.sin(p)+y*np.cos(p))

surf=ax.plot_surface(r*np.cos(t),r*np.sin(t),u*(x*np.cos(p)-y*np.sin(p)),rstride=1,cstride=1,cmap=cm.gist_rainbow_r,

                  linewidth=0,antialiased=True)

plt.show()
'''


#这个就是传统的玫瑰花，有茎秆叶子

from turtle import *
import time
 
setup(600,800,0,0)
speed(0)
penup()
seth(90)
fd(340)
seth(0)
pendown()
 
speed(5)
begin_fill()
fillcolor('red')
circle(50,30)
 
for i in range(10):
    fd(1)
    left(10)
 
circle(40,40)
 
for i in range(6):
    fd(1)
    left(3)
 
circle(80,40)
 
for i in range(20):
    fd(0.5)
    left(5)
 
circle(80,45)
 
for i in range(10):
    fd(2)
    left(1)
     
circle(80,25)
 
for i in range(20):
    fd(1)
    left(4)
 
circle(50,50)
 
time.sleep(0.1)
 
circle(120,55)
 
speed(0)
 
seth(-90)
fd(70)
 
right(150)
fd(20)
 
left(140)
circle(140,90)
 
left(30)
circle(160,100)
 
left(130)
fd(25)
 
penup()
right(150)
circle(40,80)
pendown()
 
left(115)
fd(60)
 
penup()
left(180)
fd(60)
pendown()
 
end_fill()
 
right(120)
circle(-50,50)
circle(-20,90)
 
speed(1)
fd(75)
 
speed(0)
circle(90,110)
 
penup()
left(162)
fd(185)
left(170)
pendown()
circle(200,10)
circle(100,40)
circle(-52,115)
left(20)
circle(100,20)
circle(300,20)
speed(1)
fd(250)
 
penup()
speed(0)
left(180)
fd(250)
circle(-300,7)
right(80)
circle(200,5)
pendown()
 
left(60)
begin_fill()
fillcolor('green')
circle(-80,100)
right(90)
fd(10)
left(20)
circle(-63,127)
end_fill()
 
penup()
left(50)
fd(20)
left(180)
 
pendown()
circle(200,25)
 
penup()
right(150)
 
fd(180)
 
right(40)
pendown()
begin_fill()
fillcolor('green')
circle(-100,80)
right(150)
fd(10)
left(60)
circle(-80,98)
end_fill()
 
penup()
left(60)
fd(13)
left(180)
 
pendown()
speed(1)
circle(-200,23)
 
 
 
exitonclick()

