import turtle
turtle.bgpic(bg.gif)
turtle.setup(800,600)
def a():
  for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.listen()
onkeypress(a,"space")
