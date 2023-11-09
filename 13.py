import turtle

turtle.bgpic("bg.gif")
turtle.setup(800,600)
t = turtle.Turtle()

t.shape("turtle")
t.pensize(1)
t.color("green")
turtle.addshape("rabbit.gif")

r = turtle.Turtle()
r.shape("rabbit.gif")
r.pu()
r.goto(100,100)

turtle.addshape("carrot.gif")

c = turtle.Turtle()
c.shape("carrot.gif")
c.pu()
c.goto(-100,-200)

t1 = turtle.Turtle()
t1.pu()
t1.ht()
t1.goto(-350,250)
t1.write("得分：0",font = ("微软雅黑",15))

def ahead():
    t.forward(10)

def back():
    t.backward(10)

def turnLeft():
    t.left(90)
    
def turnright():
    t.right(90)
    
def f():
    t.forward(10)

def g():
    t.backward(10)

def h():
    t.left(90)
    
def j():
    t.right(90)

def rR():
    angle = r.towards(t)
    r.seth(angle)
    r.forward(10)

    
turtle.listen()
turtle.onkeypress(ahead,"Up")
turtle.onkeypress(back,"Down")
turtle.onkeypress(turnLeft,"Left")
turtle.onkeypress(turnLeft,"Right")
turtle.onkeypress(f,"w")
turtle.onkeypress(g,"s")
turtle.onkeypress(h,"a")
turtle.onkeypress(j,"d")

while 1:
    rR()

