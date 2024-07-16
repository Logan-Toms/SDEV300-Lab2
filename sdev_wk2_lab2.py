'''
Module provides the following functions:
generate a secure password, 
calculate and format a percentage, 
calculate the number of days from today until July 4, 2025, 
use the Law of Cosines to calculate the leg of a triangle,
calculate the volume of a Right Circular Cylinder.
'''
import random
import string
from datetime import date
import math


def generate_password():
    '''This function generates a secure password based on the user's input'''
    print("\n--- Generate Secure Password ---\n")

    # Prompt the user for the length of the password
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 8: # Input validation for length
                print("Password length must be at least 8 characters long. Please try again.")
            else:
                break
        except ValueError: # Input validation for integer
            print("Invalid length. Please enter an integer value.")

    # Display the password complexity
    print("\n--- Password Complexity ---\n")
    print("1. Use lower case letters")
    print("2. Use upper and lower case letters")
    print("3. Use letters and numbers")
    print("4. Use letters, numbers and special characters")


    # Input validation for complexity
    while True:

        # Prompt the user for the complexity of the password
        complexity = input("\nEnter the complexity of the password: ")

        if complexity == "1":
            characters = string.ascii_lowercase
            break
        elif complexity == "2":
            characters = string.ascii_letters
            break
        elif complexity == "3":
            characters = string.ascii_letters + string.digits
            break
        elif complexity == "4":
            characters = string.ascii_letters + string.digits + string.punctuation
            break
        else:
            print("Invalid choice. Please try again.")

    # Generate the password
    password = "".join(random.choice(characters) for i in range(length))
    print(f"\nPassword Generated: {password}")


def calculate_percentage():
    '''This function calculates and formats a percentage'''
    print("\n--- Calculate and Format a Percentage ---\n")
    print("Details:")
    print(">  Percentage: p = n / d * 100")
    print("1. Numerator: number of parts taken out of the whole.")
    print("2. Denominator: number of total parts of the whole.\n")

    # Prompt the user for the numerator and denominator
    while True:
        try:
            numerator = int(input("1. Enter the numerator: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            denominator = int(input("2. Enter the denominator: "))
            if denominator == 0:
                raise ZeroDivisionError
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except ZeroDivisionError:
            print("Denominator cannot be zero. Please enter a non-zero value.")

    # Calculate the percentage
    percentage = numerator / denominator * 100

    # Display the percentage
    print(f"\nPercentage: {round(percentage, 2)}%")


def calculate_days():
    '''This function calculates the number of days from today until July 4, 2025'''
    print("\n--- How many days from today until July 4, 2025? ---\n")

    # Calculate the number of days
    days = (date(2025, 7, 4) - date.today()).days

    # Display the number of days
    print(f"Days: {days}")


def calculate_leg():
    '''This function uses the Law of Cosines to calculate the leg of a triangle'''
    print("\n--- Use the Law of Cosines to calculate the leg of a triangle ---\n")
    print("Details:")
    print(">  The Law of Cosines: c^2 = a^2 + b^2 - 2ab * cos(C)")
    print("1. Hypotenuse: the longest side of a right triangle.")
    print("2. Leg: the two shorter sides of a right triangle.")
    print("3. Angle: the angle between the hypotenuse and the leg.\n")

    # Prompt the user for the length of the hypotenuse, the angle and the length of the other leg
    while True:
        try:
            a = float(input("1. Enter the length of the hypotenuse: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            b = float(input("2. Enter the length of the other leg: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            c = float(input("3. Enter the angle: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Calculate the leg
    # c^2 = a^2 + b^2 - 2ab * cos(C)
    leg = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(c)))

    # Display the leg
    print(f"\nLeg = {round(leg, 2)}")


def calculate_volume():
    '''This function calculates the volume of a Right Circular Cylinder'''
    print("\n--- Calculate the volume of a Right Circular Cylinder ---\n")
    print("Details:")
    print(">  Volume: V = πr^2h")
    print("1. Radius: the distance from the center to the edge of the circular base.")
    print("2. Height: the distance from one base to the other.\n")

    # Prompt the user for the radius and height
    while True:
        try:
            radius = float(input("1. Enter the radius: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            height = float(input("2. Enter the height: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Calculate the volume
    # V = πr^2h
    volume = 3.14 * radius**2 * height

    # Display the volume
    print(f"\nVolume = {round(volume, 2)}")


def menu():
    '''This function displays the menu and prompts the user for a choice'''
    while True:
        print("\n--- Menu ---\n")
        print("a. Generate Secure Password")
        print("b. Calculate and Format a Percentage")
        print("c. How many days from today until July 4, 2025?")
        print("d. Use the Law of Cosines to calculate the leg of a triangle")
        print("e. Calculate the volume of a Right Circular Cylinder")
        print("f. Exit program")

        choice = input("\nEnter your choice: ").lower()

        if choice == "a":
            generate_password()
        elif choice == "b":
            calculate_percentage()
        elif choice == "c":
            calculate_days()
        elif choice == "d":
            calculate_leg()
        elif choice == "e":
            calculate_volume()
        elif choice == "f":
            print("\nExiting the program, thank you for visiting.\n")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
