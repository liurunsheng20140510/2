class A:
    def __init__(self,name,count):
        self.count = count
        self.name = name
        a = open("self.name" + ".txt",a)
        a.white("铅笔" + self.count + "创建账户")
    def add(self,s):
        self.count + s
        a = open("self.name" + ".txt",a)
        a.white("铅笔" + self.count + "进货" + s)
        a.close()
    def self(self,d):
        self.count - d
        a = open("self.name" + ".txt",a)
        a.white("铅笔" + self.count + "卖出" + d)
        a.close()
while 1:
    f = input("请输入你要选择的操作，1 进货，2 卖出")
    if f == 1:
        g = input("进货数量")
        add(g)
    elif f == 2:
        h = input("卖出数量")
        sell(h)
