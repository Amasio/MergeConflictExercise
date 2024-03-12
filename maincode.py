# feature2.py

from main import main, calculate_circle_area

def calculate_ellipse_area(semi_axis_a, semi_axis_b):
    return 3.14 * semi_axis_a * semi_axis_b

def feature2():
    print("This is an updated version of the Area Calculator with a new feature: ellipse calculation.")

    while True:
        shape_type = input("Enter the shape type (rectangle, circle, ellipse): ").lower()
        if shape_type == "rectangle":
            width = float(input("Enter the width: "))
            height = float(input("Enter the height: "))
            print(f"The area of the rectangle is: {calculate_rectangle_area(width, height)}")
        elif shape_type == "circle":
            radius = float(input("Enter the radius: "))
            print(f"The area of the circle is: {calculate_circle_area(radius)}")
        elif shape_type == "ellipse":
            semi_axis_a = float(input("Enter the semi-axis a: "))
            semi_axis_b = float(input("Enter the semi-axis b: "))
            print(f"The area of the ellipse is: {calculate_ellipse_area(semi_axis_a, semi_axis_b)}")
        else:
            print("Invalid shape type. Please try again.")

main()
