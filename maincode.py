# feature1.py

from main import main, calculate_rectangle_area

def calculate_square_area(side_length):
    return side_length ** 2

def feature1():
    print("This is an updated version of the Area Calculator with a new feature: square calculation.")

    while True:
        shape_type = input("Enter the shape type (rectangle, circle, square): ").lower()
        if shape_type == "rectangle":
            width = float(input("Enter the width: "))
            height = float(input("Enter the height: "))
            print(f"The area of the rectangle is: {calculate_rectangle_area(width, height)}")
        elif shape_type == "circle":
            radius = float(input("Enter the radius: "))
            print(f"The area of the circle is: {calculate_circle_area(radius)}")
        elif shape_type == "square":
            side_length = float(input("Enter the side length: "))
            print(f"The area of the square is: {calculate_square_area(side_length)}")
        else:
            print("Invalid shape type. Please try again.")

main()
