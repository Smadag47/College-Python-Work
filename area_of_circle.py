# Get pi
import math

pi = math.pi

# Function to get radius
def get_radius():
    '''Ask user for the radius of a circle'''
    radius = float(input("Enter the radius of the circle: "))
    return radius

# Use radius to calculate the area
def calculate_area(radius):
    '''Calculate the area using radius'''
    return pi * radius ** 2

# Use radius to calculate the circumference
def calculate_circumference(radius):
    '''Calculate the circumference using radius'''
    return 2 * pi * radius

# Main function
def main():
    '''Ask the user what they want to calculate, ask for the radius, and run the calculation they ask for'''
    user_choice = int(input("What would you like to calulate\n1. Area\n2. Circumference\n"))
    radius = get_radius()
    
    print(calculate_area(radius))
    print(calculate_circumference(radius))
    
if __name__ == "__main__":
    main()




