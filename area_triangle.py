#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Nov 28, 2023
# This program use a function named calc_area to calculate the area of a triangle
# and the function would get called to def main.


# Making a variable named calc_area
def calc_area(base, height):
    # Calculate the area of the triangle using the formula: (1/2) * base * height
    area = 1 / 2 * base * height
    # Display the calculated area
    print("The area of the triangle is {} cm^2".format(area))


def main():
    base = input("Enter the base of the triangle : ")

    height = input("Enter the the height for the triangle : ")

    try:
        # Attempt to convert user inputs to float
        base = float(base)
        height = float(height)
        calc_area(base, height)

    except ValueError as e:
        print("{} Is not a valid input".format(e))


if __name__ == "__main__":
    main()
