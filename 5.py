s = ""
d = ""
f = ""
a = input("一串数字")
for i in a:
  if i % 2 == 0:
    if i not in s:
      s.append(i)
    elif i in s:
      i += 1
  elif i % 2 == 1:
    if i not in d:
      d.append(o)
    elif i in d:
      d += 1
g = len(a)
f.append(g)
