a = ([['Rhia',10,20,30,40,50],
      ['Alan',75,80,75,85,100],
      ['Smith',80,80,80,90,95]])

for i in a:
    print(i[:2])

a[2:3] = [['Sam',82,79,88,97,99]]
print(a)

a[0][3] = 95
print(a)

a.append(['Sandy',73, 80, 85, 87, 98])
print(a)