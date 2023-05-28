import matplotlib.pyplot as plt

def draw_ellipse(xc, yc, a, b):
    x = 0
    y = b
    p = b**2 - a**2*b + a**2/4
    dx = 2*b**2*x
    dy = 2*a**2*y

    #region 1
    plt.scatter(xc+x, yc+y, color='black')
    plt.scatter(xc-x, yc+y, color='black')
    plt.scatter(xc+x, yc-y, color='black')
    plt.scatter(xc-x, yc-y, color='black')

    #region 2
    while dx < dy:
        x += 1
        dx += 2*b**2
        if p < 0:
            p += b**2*dx + b**2
        else:
            y -= 1
            dy -= 2*a**2
            p += b**2*dx - a**2*dy + b**2

        plt.scatter(xc+x, yc+y, color='black')
        plt.scatter(xc-x, yc+y, color='black')
        plt.scatter(xc+x, yc-y, color='black')
        plt.scatter(xc-x, yc-y, color='black')

    #region 3
    p = b**2*(x+0.5)**2 + a**2*(y-1)**2 - a**2*b**2
    while y > 0:
        y -= 1
        dy -= 2*a**2
        if p > 0:
            p += a**2 - 2*a**2*y
        else:
            x += 1
            dx += 2*b**2
            p += b**2*dx - a**2*dy + a**2

        plt.scatter(xc+x, yc+y, color='black')
        plt.scatter(xc-x, yc+y, color='black')
        plt.scatter(xc+x, yc-y, color='black')
        plt.scatter(xc-x, yc-y, color='black')

# take user input for center point, major and minor axis lengths
xc = int(input("Enter the x-coordinate of the center point: "))
yc = int(input("Enter the y-coordinate of the center point: "))
a = int(input("Enter the length of the major axis: "))
b = int(input("Enter the length of the minor axis: "))

draw_ellipse(xc, yc, a, b)
plt.show()
