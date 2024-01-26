import turtle
import time
import random

turtle.bgpic("背景.gif")
turtle.setup(700, 700)
turtle.tracer(False)

# 创建鸡蛋
turtle.register_shape("egg.gif")
egg = turtle.Turtle()
egg.shape("egg.gif")
egg.penup()
egg.goto(-200, -200)

turtle.register_shape("病菌.gif")
bj1 = turtle.Turtle()
bj1.shape("病菌.gif")
bj1.penup()
bj1.goto(270, -50)

turtle.register_shape("病菌.gif")
bj2 = turtle.Turtle()
bj2.shape("病菌.gif")
bj2.penup()
bj2.goto(20, -130)
# 创建小蛇
turtle.register_shape("head1.gif")
turtle.register_shape("head2.gif")
turtle.register_shape("head3.gif")
turtle.register_shape("head4.gif")
turtle.register_shape("body.gif")
snakeList = []
for i in range(5):
    t = turtle.Turtle()
    t.shape("turtle")
    t.setheading(180)
    t.penup()
    t.goto(i * 20, 0)  # 将小海龟一字排开
    if i == 0:
        t.shape("head1.gif")
    else:
        t.shape("body.gif")
    snakeList.append(t)

# 记录长度
word = turtle.Turtle()
word.penup()
word.goto(-270, 310)
word.color("white")
word.write("5", font=("微软雅黑", 20))
word.hideturtle()

# 刷新窗口
turtle.update()

# 蛇类
class Snake():
    def __init__(self, snakeList):
        self.snakeList = snakeList
        self.length = len(snakeList)
        self.flag = "left"  # 贪吃蛇当前的移动方向

    # 转向：左
    def left(self):
        if self.flag != "right":
            self.flag = "left"

    # 转向：上
    def up(self):
        if self.flag != "down":
            self.flag = "up"

    # 转向：右
    def right(self):
        if self.flag != "left":
            self.flag = "right"

    # 转向：下
    def down(self):
        if self.flag != "up":
            self.flag = "down"

    # 向左移动
    def goLeft(self):
        # 获取列表中第一只小海龟的坐标
        x = self.snakeList[0].xcor()
        y = self.snakeList[0].ycor()
        # 删除列表中的最后一只小海龟
        t = self.snakeList.pop(-1)
        t.hideturtle()
        # 在列表的开头加入一只新的小海龟
        t1 = turtle.Turtle()
        t1.shape("head1.gif")
        self.snakeList.insert(0, t1)
        t1.penup()
        t1.goto(x - 20, y)
        # 将列表中第二只小海龟的形状设置为身体部分
        self.snakeList[1].shape("body.gif")

        turtle.update()

    # 向上移动
    def goUp(self):
        # 获取列表中第一只小海龟的坐标
        x = self.snakeList[0].xcor()
        y = self.snakeList[0].ycor()
        # 删除列表中的最后一只小海龟
        t = self.snakeList.pop(-1)
        t.hideturtle()
        # 在列表的开头加入一只新的小海龟
        t1 = turtle.Turtle()
        t1.shape("head2.gif")
        self.snakeList.insert(0, t1)
        t1.penup()
        t1.goto(x, y + 20)
        # 将列表中第二只小海龟的形状设置为身体部分
        self.snakeList[1].shape("body.gif")

        turtle.update()

    # 向右移动
    def goRight(self):
        # 获取列表中第一只小海龟的坐标
        x = self.snakeList[0].xcor()
        y = self.snakeList[0].ycor()
        # 删除列表中的最后一只小海龟
        t = self.snakeList.pop(-1)
        t.hideturtle()
        # 在列表的开头加入一只新的小海龟
        t1 = turtle.Turtle()
        t1.shape("head3.gif")
        self.snakeList.insert(0, t1)
        t1.penup()
        t1.goto(x + 20, y)
        # 将列表中第二只小海龟的形状设置为身体部分
        self.snakeList[1].shape("body.gif")

        turtle.update()

    # 向下移动
    def goDown(self):
        # 获取列表中第一只小海龟的坐标
        x = self.snakeList[0].xcor()
        y = self.snakeList[0].ycor()
        # 删除列表中的最后一只小海龟
        t = self.snakeList.pop(-1)
        t.hideturtle()
        # 在列表的开头加入一只新的小海龟
        t1 = turtle.Turtle()
        t1.shape("head4.gif")
        self.snakeList.insert(0, t1)
        t1.penup()
        t1.goto(x, y - 20)
        # 将列表中第二只小海龟的形状设置为身体部分
        self.snakeList[1].shape("body.gif")

        turtle.update()

    # 吃鸡蛋
    def eat(self):
        # 获取鸡蛋坐标
        eggX = egg.xcor()
        eggY = egg.ycor()

        # 获取蛇头坐标
        headX = self.snakeList[0].xcor()
        headY = self.snakeList[0].ycor()

        if eggX == headX and eggY == headY:

            eggX = random.randint(-17,17)*20
            eggY = random.randint(-17,17)*20
            
            bj1X = random.randint(-17,17)*20
            bj1Y = random.randint(-17,17)*20

            bj2X = random.randint(-17,17)*20
            bj2Y = random.randint(-17,17)*20

            egg.goto(eggX, eggY)
            bj1.goto(bj1X, bj1Y)
            bj2.goto(bj2X, bj2Y)
            t =  turtle.Turtle()
            t.shape("body.gif")
            self.snakeList.append(t)
            self.length += 1
            word.clear()
            word.write(self.length, font=("微软雅黑", 20))

            turtle.update()

    def checkBound(self):
        headX = self.snakeList[0].xcor()
        headY = self.snakeList[0].ycor()
        if headX < -350 or headX > 350 or headY < -350 or headY > 350:
            return True
            
    def a(self):
        headX = self.snakeList[0].xcor()
        headY = self.snakeList[0].ycor()
        if headX = bj1X and headY = bj1Y or headX = bj2X and headY = bj2Y
            return True


    def checkBody(self):
        headX = self.snakeList[0].xcor()
        headY = self.snakeList[0].ycor()
        for i in range(1,len(self.snakeList)):
            if headX == self.snakeList[i].xcor() and headY == self.snakeList[i].ycor():
                return 1
            
    

s = Snake(snakeList)

turtle.listen()
turtle.onkeypress(s.left, "Left")
turtle.onkeypress(s.up, "Up")
turtle.onkeypress(s.right, "Right")
turtle.onkeypress(s.down, "Down")



while True:
    s.eat()
    if s.flag == "left":
        s.goLeft()
    elif s.flag == "up":
        s.goUp()
    elif s.flag == "right":
        s.goRight()
    elif s.flag == "down":
        s.goDown()
        
    if s.checkBound():
        break

    if s.checkBody():
        break
    
    if a():
        break



    time.sleep(0.1)

time.sleep(2)
turtle.bye()
