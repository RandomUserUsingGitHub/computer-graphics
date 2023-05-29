import matplotlib.pyplot as plt
import math
import numpy as np
import os


# A function to do the matrix multiplication and calculate them
# ---------------------------start------------------------------
def calculate(matrix):

    for idx, val in enumerate(x):
        current = np.array([[x[idx]],
                            [y[idx]],
                            [1]], dtype=float)
        dot = np.dot(matrix, current)
        x[idx] = round(dot[0][0])
        y[idx] = round(dot[1][0])
# ----------------------------end-------------------------------



# Functions to set the matrices and call the calculate function
# ---------------------------start------------------------------
def original():
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title("Original")

def init_transform():
    x_transition = input("enter translation x: ")
    y_transition = input("enter translation y: ")
    translation_matrix = np.array([[1,0,x_transition],
                                   [0,1,y_transition],
                                   [0,0,1]], dtype=float)
    calculate(translation_matrix)

def transform_for_rotation(x_transition,y_transition):
    translation_matrix = np.array([[1,0,x_transition],
                                   [0,1,y_transition],
                                   [0,0,1]], dtype=float)
    calculate(translation_matrix)
    
def init_rotation():
    tetha = float(input("enter rotaion in degrees: "))
    tetha = math.radians(tetha)
    cos_angle = math.cos(tetha)
    sin_angle = math.sin(tetha)
    x = int(input("around what x-axis: "))
    y = int(input("around what y-axis: "))
    transform_for_rotation(-x,-y)
    rotation_matrix = np.array([[cos_angle,-sin_angle,0],
                                [sin_angle, cos_angle,0],
                                [    0    ,     0    ,1]], dtype=float)
    calculate(rotation_matrix)
    transform_for_rotation(x,y)

def init_resize():
    x_resize = input("enter resize value of x-axis: ")
    y_resize = input("enter resize value of y-axis: ")
    
    resize_matrix = np.array([[x_resize,0,0],
                              [0,y_resize,0],
                              [0,0,1]], dtype=float)
    calculate(resize_matrix)

def init_reflection():
    os.system('cls' if os.name == 'nt' else 'clear')
    action = input("select reflection:\n1) about X-axis\n2) about Y-axis\n3) about origin\n4) about y = x\nyour option: ")
    match action:
        case '1':
            reflection_matrix = np.array([[ 1, 0, 0],
                                          [ 0,-1, 0],
                                          [ 0, 0, 1]])
        case '2':
            reflection_matrix = np.array([[-1, 0, 0],
                                          [ 0, 1, 0],
                                          [ 0, 0, 1]])
        case '3':
            reflection_matrix = np.array([[-1, 0, 0],
                                          [ 0,-1, 0],
                                          [ 0, 0, 0]])
        case '4':
            reflection_matrix = np.array([[ 0, 1, 0],
                                          [ 1, 0, 0],
                                          [ 0, 0, 1]])
    calculate(reflection_matrix)
# ----------------------------end-------------------------------



# Functions to get the user input based on their desired action
# ---------------------------start------------------------------
def get_user_input():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("previos values:")
    for idx in range(sides):
        print(f"-> i{idx}({x[idx]},{y[idx]})")
    print("----------------")
    action = input("select action:\n1) transition\n2) rotation\n3) resize\n4) reflection\nyour option: ")
    match action:
        case '1':
            init_transform()
        case '2':
            init_rotation()
        case '3':
            init_resize()
        case '4':
            init_reflection()
    print("----------------")
    print("current values:")
    for idx in range(sides):
        print(f"-> i{idx}({x[idx]},{y[idx]})")
    print("----------------")
# ----------------------------end-------------------------------



#                          main code
# ---------------------------start------------------------------
x = []
y = []
sides = int(input(f"How many sides the shape should have? "))
for idx in range(sides):
    x.append(int(input(f"Enter x-coordinate of point {idx+1}: ")))
    y.append(int(input(f"Enter y-coordinate of point {idx+1}: ")))
    print(f"-> i{idx}({x[idx]},{y[idx]})")
    print("---------------------------------")
x.append(x[0])
y.append(y[0])

input("press any key to continue...\n")
original()
get_user_input()

while(input("continue?(1/0) ----> ") == '1'):
        get_user_input()

plt.figure()
plt.plot(x, y, marker='o')
plt.title("after matrices")
plt.show()
# ----------------------------end-------------------------------
