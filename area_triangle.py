# !/user/bin/env.python3
# Created By: Jeremiah omoike
# Date: Nov. 24, 2022
# This program Asks user for the length  and the height of a triangle and calculates the area


def calc_area(base_float, height_float):
    area = base_float * height_float / 2
    print("The area of a triangle with the base of {}cm,".format(base_float))
    print()
    # Displays the area of the triangle to the user 
    print("and the height of {}cm, is {:.2f} cm^2".format(height_float, area))


def main():

    print("Hello, welcome to my area of triangle program")
    print()
    # gets base and height from user 
    base_as_string = input(" please enter the base of your triangle (cm): ")
    height_as_string = input(" please enter the height of your triangle (cm): ")
    # Checks is user entered a string or any other invalid input
    try:
        base_as_float_user = float(base_as_string)
        height_as_float_user = float(height_as_string)
        # checks if user number is more than 0 
        if base_as_float_user > 0 and height_as_float_user > 0:
        # calculate the area  of the triangle. b x h /2
            calc_area(base_as_float_user, height_as_float_user)
        else:
            print()
        
            print("The base and the height of the triangle have to be more than 0")
    except Exception:
        print()
        print("In valid error. only numbers can be accepted ")


if __name__ == "__main__":
    main()
