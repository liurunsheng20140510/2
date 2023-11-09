import turtle
import random
turtle.addshape("吸铁石.gif")
turtle.addshape("钉子.gif")
t = turtle.Turtle()
t.shape("吸铁石.gif")
t1 = turtle.Turtle()
t1.shape("钉子.gif")
a = random.randint(0,800)
b = random.randint(0,800)

t.goto(a,b)
d = towards(t)
t1.setheading(d)
while 1:
    t1.forward(100)
