import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def clip_line(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    INSIDE = 0
    LEFT = 1
    RIGHT = 2
    BOTTOM = 4
    TOP = 8

    outcode1 = compute_outcode(x1, y1, x_min, y_min, x_max, y_max)
    outcode2 = compute_outcode(x2, y2, x_min, y_min, x_max, y_max)
    accept = False

    while True:
        if outcode1 == 0 and outcode2 == 0:
            accept = True
            break
        elif outcode1 & outcode2 != 0:
            break
        else:
            x = 0
            y = 0
            outcode_out = outcode1 if outcode1 != 0 else outcode2

            if outcode_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif outcode_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif outcode_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif outcode_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if outcode_out == outcode1:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1, x_min, y_min, x_max, y_max)
            else:
                x2, y2 = x, y
                outcode2 = compute_outcode(x2, y2, x_min, y_min, x_max, y_max)

    if accept:
        fig, ax = plt.subplots()
        ax.add_patch(Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, edgecolor='red', facecolor='none'))
        plt.plot([x1, x2], [y1, y2], color='blue')
        plt.xlim(x_min - 1, x_max + 1)
        plt.ylim(y_min - 1, y_max + 1)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid(True)
        plt.show()

x_min = float(input("Enter the minimum x-coordinate of the rectangle: "))
y_min = float(input("Enter the minimum y-coordinate of the rectangle: "))
x_max = float(input("Enter the maximum x-coordinate of the rectangle: "))
y_max = float(input("Enter the maximum y-coordinate of the rectangle: "))

x1 = float(input("Enter the x-coordinate of the first endpoint of the line: "))
y1 = float(input("Enter the y-coordinate of the first endpoint of the line: "))
x2 = float(input("Enter the x-coordinate of the second endpoint of the line: "))
y2 = float(input("Enter the y-coordinate of the second endpoint of the line: "))

def compute_outcode(x, y, x_min, y_min, x_max, y_max):
    code = 0
    if x < x_min:
        code |= 1  # LEFT
    elif x > x_max:
        code |= 2  # RIGHT
    if y < y_min:
        code |= 4  # BOTTOM
    elif y > y_max:
        code |= 8  # TOP
    return code

clip_line(x1, y1, x2, y2, x_min, y_min, x_max, y_max)
