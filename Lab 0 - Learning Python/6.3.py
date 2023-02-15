def Count(l):
  d = dict()
  print(d)
  for item in l:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1
  print(d)
l = [11, 45, 8, 11, 23, 45, 23, 45, 89]
Count(l)
