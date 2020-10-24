  
points = [
    {'x' : 1, 'y' : 1},
    {'x' : 1, 'y' : 1},
    {'x' : 1, 'y' : -1},
    {'x' : -1, 'y' : -2},
    ]
temp = []

for point in points:
    x = abs(point['x'])
    y = abs(point['y'])
    temp.append([x, y]) 
a = []
for i in temp:
    if i not in a:
        a.append(i)
print(len(a))
