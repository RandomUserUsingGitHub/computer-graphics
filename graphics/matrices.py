import matplotlib.pyplot as plt
import math
import numpy as np

def original():
    x.append(x[0])
    y.append(y[0])

    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title("Original")

def calculate(matrix):

    for idx, val in enumerate(x):
        current = np.array([[x[idx]],
                            [y[idx]],
                            [1]], dtype=float)
        dot = np.dot(matrix, current)
        x[idx] = dot[0]
        y[idx] = dot[1]

    if(input("continue?(1/0) ----> ") == '1'):
        get_user_input()
    

def init_transform():
    x_transition = input("enter translation x: ")
    y_transition = input("enter translation y: ")
    translation_matrix = np.array([[1,0,x_transition],
                                   [0,1,y_transition],
                                   [0,0,1]], dtype=float)
    calculate(translation_matrix)

def init_rotation():
    tetha = float(input("enter rotaion in degrees: "))
    tetha = math.radians(tetha)
    x = int(input("around what x-axis: "))
    y = int(input("around what y-axis: "))
    rotation_matrix = np.array([[math.cos(tetha),-math.sin(tetha),x],
                                [math.sin(tetha), math.cos(tetha),y],
                                [       0       ,        0       ,1]],
                                dtype=float)
    calculate(rotation_matrix)

def init_resize():
    x_resize = input("enter resize value of x-axis: ")
    y_resize = input("enter resize value of y-axis: ")
    
    resize_matrix = np.array([[x_resize,0,0],
                                   [0,y_resize,0],
                                   [0,0,1]], dtype=float)
    calculate(resize_matrix)

def get_user_input():
    action = input("select action:\n1) transition\n2) rotation\n3) resize\n")
    match action:
        case '1':
            init_transform()
        case '2':
            init_rotation()
        case '3':
            init_resize()

# Get user input for the three points of the triangle
x = []
y = []
sides = int(input(f"How many sides the shape should have? "))
for idx in range(sides):
    print(idx)
    x.append(int(input(f"Enter x-coordinate of point {idx+1}: ")))
    y.append(int(input(f"Enter y-coordinate of point {idx+1}: ")))
    print(f"i{idx}({x[idx]},{y[idx]})")
    print("---------------------------------")
x.append(x[0])
y.append(y[0])

original()
get_user_input()
plt.figure()
plt.plot(x, y, marker='o')
plt.title("after matrices")
plt.show()
