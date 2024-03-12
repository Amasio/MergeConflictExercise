def main():
	def calculate_circle_area(radius):
	    return 3.14 * radius ** 2

        def calculate_rectangle_area(width, height):
                return height * width

        def calculate_square_area(side_length):
            return side_length ** 2

        def calculate_ellipse_area(semi_axis_a, semi_axis_b):
            return 3.14 * semi_axis_a * semi_axis_b
            
        while True:
            shape_type = input("Enter the shape type (rectangle, circle, ellipse,square): ").lower()
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
            elif shape_type == "ellipse":
                semi_axis_a = float(input("Enter the semi-axis a: "))
                semi_axis_b = float(input("Enter the semi-axis b: "))
                print(f"The area of the ellipse is: {calculate_ellipse_area(semi_axis_a, semi_axis_b)}")
            else:
                print("Invalid shape type. Please try again.")

main()
