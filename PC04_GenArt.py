#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:06:03 2021

@author: ianrowland
"""

import turtle, math, random

#turtle for circles
cir = turtle.Turtle()

#turtle for squares
sq = turtle.Turtle()


#I had no reason to do this, just kept messing it up so I just did this
hi=turtle.Screen()

backColor = ["black","AliceBlue","cornsilk", "azure3", "lavenderblush","PapayaWhip","midnightblue","darkslategray","palegoldenrod"]
panel = hi.bgcolor(random.choice(backColor))

cir.speed(10)
sq.speed(10)

#turtle colors weren't working, sites told me to do this
cir.screen.colormode(255)
sq.screen.colormode(255)

cir.hideturtle()
sq.hideturtle()


    


numIter2 = random.randint(9,25) 

#A for loop that draws between 3-20 filled circles of random areas, colors, sizes, and line widths.
for iteration in range(numIter2):
   cir.up()
   
   cir.goto(random.randint(-300,300),random.randint(-300,300))   
   color = [(255,255,255),(102,255,255),(255,161,240),(255,102,102),(153,204,255),(123,104,238),(255,222,173)]
   cir.color(random.choice(color))
   cir.fillcolor(random.choice(color))
   cir.begin_fill()
  
   cir.pensize(random.randint(2,4))
   radius = random.randint(4,75)
   cir.down()
   cir.circle(radius)
   cir.up()
   cir.end_fill()
  


numIter = random.randint(2,16)

#For loop for 2-15 random, non-filled circles. Once again of random areas, colors, sizes, and line widths.
for i in range(numIter):
   cir.up()
  
   cir.goto(random.randint(-300,300),random.randint(-300,300))
   cir.pensize(random.randint(2,5))
   color = [(255,255,255),(125,255,255),(230,169,255),(255,102,102),(123,104,238)]
   cir.color(random.choice(color))
   radius = random.randint(4,55)
   cir.down()
   cir.circle(radius)
   cir.up()


   
sides = 4
numIter3 = random.randint(4,6)

#This for loop draws a random number of squares, in random areas, with random colors, sizes, and line widths
for iteration2 in range(numIter3):
   sq.up()
   sq.goto(random.randint(-300,300),random.randint(-300,300))
   
   sq.pensize(random.randint(2,5))
   color = [(255,255,255),(0,255,255),(255,161,240),(204,204,255),(123,104,238)]
   sq.color(random.choice(color))
   sq.fillcolor(random.choice(color))
   sq.begin_fill()

   size = random.randint(10,100)
   sq.right(45)
   sq.down()
   for iteration1 in range(sides):
       sq.forward(size)
       sq.right(90)
   sq.up()
   sq.end_fill()



sq.done()

cir.done()

    