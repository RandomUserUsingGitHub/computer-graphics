import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

xmin, ymin = 100, 100
xmax, ymax = 300, 300

Xa, Ya = 200, 50
Xb, Yb = 150, 350

dx = Xb - Xa
dy = Yb - Ya

p = {
    1 : -dx,
    2 : dx,
    3 : -dy,
    4 : dy, 
}

q = {
    1 : Xa - xmin,
    2 : xmax - Xa,
    3 : Ya - ymin,
    4 : ymax - Ya,
}

t1 = 0
t2 = 1

for i in range(1, 5):

    if p[i] == 0:
        if (dx == 0):
            print("Line is parallel to X pivot")
        elif (dy == 0):
            print("Line is parallel to Y pivot")
        break

    elif  p[i] < 0: #OIP
        r = (q[i] / p[i])
        t1 = max(t1, r)
        print(f"r={r}, t1={t1}\n")

    elif p[i] > 0: #IOP
        r = q[i] / p[i]
        t2 = min(t2, r)
        print(f"r={r}, t2={t2}\n")

   
if t1 > t2:
    print("Rejected.")
else:
    print(f"Clipped line is between ({t1}, {t2})")

if t1 == 0:
    O1x, O1y = Xa, Ya
else:
    O1x = Xa + (t1 * dx)
    O1y = Ya + (t1 * dy)

if t2 == 1:
    O2x, O2y = Xb, Yb
else:
    O2x = Xa + (t2 * dx)
    O2y = Ya + (t2 * dy)


print(f"O1({O1x},{O1y})")
print(f"O2({O2x},{O2y})")

fig, ax = plt.subplots()
ax.add_patch(Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, edgecolor='red', facecolor='none'))
plt.plot([O1x, O2x], [O1y, O2y], color='blue')
plt.xlim(xmin - 1, xmax + 1)
plt.ylim(ymin - 1, ymax + 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
