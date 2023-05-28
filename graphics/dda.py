import matplotlib.pyplot as plt

x1 = int(input("Enter the value of x1: "))
y1 = int(input("Enter the value of y1: "))
print(f"point 1: ({x1},{y1})")
x2 = int(input("Enter yhe value of x2: "))
y2 = int(input("Enter the value of y2: "))
print(f"point 2: ({x2},{y2})")
print("-----------------------------")


dx = x2 - x1
dy = y2 - y1

if abs(dx) > abs(dy) : 
    steps = abs(dx)
else:
    steps = abs(dy)

xincrement = dx/steps
yincrement = dy/steps

xcoordinates = [x1]
ycoordinates = [y1]

for i in range(steps):
    i+=1
    x1 = x1 + xincrement
    y1 = y1 + yincrement
    xcoordinates.append(round(x1))
    ycoordinates.append(round(y1))
    print("x1=" , "{:.2f}".format(x1) , " , y1=" , "{:.2f}".format(y1))

plt.plot(xcoordinates, ycoordinates,color='black',linestyle='dashed',marker='o')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("DDA Algoritm")
plt.show()