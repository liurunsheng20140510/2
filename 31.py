a = []
for i in range(1000):
    a.append(0)
for i in range(1,1001):
    if i % 5 == 0:
        a[i-1] += 1
    if i % 7 == 0:
        a[i-1] += 1
    if i % 9 == 0:
        a[i-1] += 1
    if i % 12 == 0:
        a[i-1] += 1
b = max(a)
print("最多按了{}下".format(b))
c = min(a)
print("最少按了{}下".format(c))
d = a.count(0)
e = a.count(1)
f = a.count(2)
print("最后亮了{}盏灯".format(d+e+f))
