a = []
for i in range(1000):
    a.append(0)
for i in range(1001):
    if i % 5 == 0:
        a[i-1] += 1
    if i % 7 == 0:
        a[i-1] += 1
    if i % 9 == 0:
        a[i-1] += 1
    if i % 12 == 0:
        a[i-1] += 1
print(a)
