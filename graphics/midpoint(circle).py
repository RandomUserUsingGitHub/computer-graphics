import matplotlib.pyplot as plt

plt.title("midpoint Algoritm")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

x_cent = int(input("Enter x-coordinates of the center: "))
y_cent = int(input("Enter y-coordinates of the center: "))
r = int(input("Enter the radius of the circle: "))
print("-----------------------------")


x1 = 0
y1 = r
p0 = 1 - r
pk = p0
xcoordinates = [x1]
ycoordinates = [y1]

def pk_plus1(pk):
    global x1, y1
    if(pk >= 0):
        x1 = x1 + 1
        y1 = y1 - 1
        return pk + 2*x1 - 2*y1 + 1
    elif(pk < 1):
        x1 = x1 + 1
        return pk + 2*x1 + 1
    
def full_circle():
    dots = len(xcoordinates)
    for idx in range(dots):
        # quarter2
        xcoordinates.append(+(ycoordinates[idx]))
        ycoordinates.append(+(xcoordinates[idx]))
        # quarter3
        xcoordinates.append(+(ycoordinates[idx]))
        ycoordinates.append(-(xcoordinates[idx]))
        # quarter4
        xcoordinates.append(+(xcoordinates[idx]))
        ycoordinates.append(-(ycoordinates[idx]))
        # quarter5 
        xcoordinates.append(-(xcoordinates[idx]))
        ycoordinates.append(-(ycoordinates[idx]))
        # quarter6 
        xcoordinates.append(-(ycoordinates[idx]))
        ycoordinates.append(-(xcoordinates[idx]))
        # quarter7 
        xcoordinates.append(-(ycoordinates[idx]))
        ycoordinates.append(+(xcoordinates[idx]))
        # quarter8
        xcoordinates.append(-(xcoordinates[idx]))
        ycoordinates.append(+(ycoordinates[idx]))

def transition():
    for idx in range(len(xcoordinates)):
        xcoordinates[idx] += x_cent
        ycoordinates[idx] += y_cent
        
    
while(x1 < y1):
    pk = pk_plus1(pk)
    xcoordinates.append(x1)
    ycoordinates.append(y1)
    print("x1=" , x1 , " , y1=" , y1)

full_circle()

show_transition = int(input("show transition? (1/0)" ))

if(show_transition == 1):
    plt.scatter(xcoordinates,ycoordinates,color='grey',s=3)
    plt.plot((0,x_cent),(0,y_cent),color='blue',linestyle='dashed',marker='o')

transition()

plt.scatter(xcoordinates,ycoordinates,color='black')
plt.axis('equal')
plt.show()


