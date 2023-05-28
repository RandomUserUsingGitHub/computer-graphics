import matplotlib.pyplot as plt


plt.title("Bresenham Algoritm")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")


x1 = int(input("Enter the value of x1: "))
y1 = int(input("Enter the value of y1: "))
print(f"point 1: ({x1},{y1})")
x2 = int(input("Enter yhe value of x2: "))
y2 = int(input("Enter the value of y2: "))
print(f"point 2: ({x2},{y2})")
print("-----------------------------")


dx = x2 - x1
dy = y1 - y1
m = abs(dy)/abs(dx)

xcoordinates = [x1]
ycoordinates = [y1]

if(m <= 1):
    p0 = 2*dy - dx
else:
    p0 = 2*dx - dy

    
pk = p0


def Pk_plus1(pk):
    global x1,y1
    # step on X
    if(pk >= 0 and m <= 1):
        x1 = x1 + 1
        y1 = y1 + 1
        return pk + 2*abs(dy) - 2*abs(dx)
    elif(pk < 0 and m <= 1):
        x1 = x1 + 1
        return pk + 2*abs(dy)
    
    # step on Y
    elif(pk >= 0 and m > 1):
        x1 = x1 + 1
        y1 = y1 + 1
        return pk + 2*abs(dx) - 2*abs(dy)
    elif(pk < 0 and m > 1):
        y1 = y1 + 1
        return pk + 2*abs(dx)
    

while True:
    pk = Pk_plus1(pk)
    xcoordinates.append(x1)
    ycoordinates.append(y1)
    print("x1=" , x1 , " , y1=" , y1)
    if(x1 == x2 and y1 == y2):
        break


plt.plot(xcoordinates, ycoordinates,color='black',linestyle='dashed',marker='o')
plt.show()