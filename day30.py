from turtle import *
from colorsys import hsv_to_rgb

tracer(5)
bgcolor("black")
pensize(2)
speed(0)

h = 1
for i in range(140):
    h -= 0.0071
    color(hsv_to_rgb(h, 1, 1))
    
    penup()
    goto(20, 10)
    pendown()
    
    right(70)
    forward(i * 2)
    circle(i * 2, -10)
    left(100)
    
    penup()
    forward(i)
    pendown()
    
    circle(90, -90)
    right(230)

done()
