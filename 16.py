# to draw an ellipse
import turtle

t = turtle.Turtle()
w = turtle.Screen()
w.screensize(2000,2000)
turtle.title("ellipse")

# to get radius from user
a = int(input('enter smaller radius: '))
b = int(input('enter taller  radius: '))

t.pencolor('gray')
t.begin_fill()
t.pensize(1)
t.speed(1)

#tilt the shape to 45
t.setheading(45)

# for drawing whole shape with tow arcs 
# turtle.circle(radius, extent=90, steps=None)
for i in range(2):
    t.circle(a,90)  
    t.circle(b,90)

w.bgcolor('black')

t.fillcolor('purple')
t.end_fill()

w.mainloop()