import matplotlib.pyplot as plt
import math

plt.title("midpoint Algoritm")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

print("(x + tx/a)^2 + (y + ty/b)^2 = c")
tx = int(input("tx = "))
ty = int(input("ty = "))
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(f"((x{tx:+})^2 / ({a*a*c}) + ((y{ty:+})^2 / {b*b*c}) = 1")
print("-----------------------------")

a = round(math.sqrt(a*a*c))
b = round(math.sqrt(b*b*c))
x = 0
y = b
xcoordinates = [x]
ycoordinates = [y]
p0 = b*b + (a*a)/4 - a*a*b
pk = p0

def calculate_m(x,y):
    global dx,dy
    dx = 2*b*b*x
    dy = 2*a*a*y

def pk_plus1(pk,region):
    global x,y
    if(region == 1):
        if(pk >= 0):
            x = x + 1
            y = y - 1
            return pk + 2*b*b*x - 2*a*a*y + b*b
        elif(pk < 0):
            x = x + 1
            return pk + 2*b*b*x + b*b
    elif(region == 2):
        if(pk >= 0):
            y = y - 1
            return pk - 2*a*a*y + a*a
        elif(pk < 0):
            x = x + 1
            y = y - 1
            return pk - 2*a*a*y + 2*b*b*x + a*a
        
def full_ellipse():
    dots = len(xcoordinates)
    for idx in range(dots):
        # quarter2
        xcoordinates.append(+(xcoordinates[idx]))
        ycoordinates.append(-(ycoordinates[idx]))
        # quarter3
        xcoordinates.append(-(xcoordinates[idx]))
        ycoordinates.append(-(ycoordinates[idx]))
        # quarter4
        xcoordinates.append(-(xcoordinates[idx]))
        ycoordinates.append(+(ycoordinates[idx]))

def transition():
    for idx in range(len(xcoordinates)):
        xcoordinates[idx] -= tx
        ycoordinates[idx] -= ty


calculate_m(x,y)
while(dy >= dx):
    pk = pk_plus1(pk,1)
    xcoordinates.append(x)
    ycoordinates.append(y)
    print("x=" , x , " , y=" , y)
    calculate_m(x,y)
p0 = b*b*((float(x)+0.5)**2) + a*a*((y-1)**2) - a*a*b*b
pk = p0
while(dy < dx and y != 0):
    pk = pk_plus1(pk,2)
    xcoordinates.append(x)
    ycoordinates.append(y)
    print("x=" , x , " , y=" , y)
    calculate_m(x,y)

full_ellipse()
transition()

plt.scatter(xcoordinates,ycoordinates,color='black')
plt.scatter(-tx,-ty,color='grey')
plt.axis('equal')
plt.show()



