# main.py

def main():
    print("Welcome to the Area Calculator!")
    while True:
        shape_type = input("Enter the shape type (rectangle, circle): ").lower()
        if shape_type == "rectangle":
            width = float(input("Enter the width: "))
            height = float(input("Enter the height: "))
            print(f"The area of the rectangle is: {calculate_rectangle_area(width, height)}")
        elif shape_type == "circle":
            radius = float(input("Enter the radius: "))
            print(f"The area of the circle is: {calculate_circle_area(radius)}")
        else:
            print("Invalid shape type. Please try again.")

def calculate_rectangle_area(width, height):
    return width * height

def calculate_circle_area(radius):
    return 3.14 * radius ** 2

if __name__ == "__main__":
    main()
