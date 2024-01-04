#define the functions for each calculation
def distance_calc():
    '''Takes the speed and time, then calulates distance'''
    speed = float(input("What is the Speed in Km/h: ")) 
    time = float(input("What is the Time in hours: "))
    distance = round(speed * time, 2)
    print(f"Traveling for {time} hours at {speed}Km/h\
           you will travel {distance}Km")


def speed_calc():
    '''Takes the distance and time, then calulates speed'''
    distance = float(input("What is the Distance in Km: ")) 
    time = float(input("What is the Time in hours: "))
    speed = round(distance / time, 2)
    print(f"If you travel {distance}Km in {time} hours,\
           you are traveling at {speed}Km/h")


def time_calc():
    '''Takes the distance and speed, then calulates time'''
    distance = float(input("What is the Distance in Km: "))
    speed = float(input("What is the Speed in Km/h: ")) 
    time = round(distance / speed, 2)
    print(f"If you travel {distance}Km at {speed}Km/h,\
           it will take you {time} hours to reach your destination")

#Ask the user to select a calulation
required_calc = int(input("What are you trying to calculate\n\
1. Speed\n\
2. Distance\n\
3. Time\n\
Select 1, 2, or 3: "))

#Process the users input and call the requested function
if required_calc == 1:
    speed_calc()
elif required_calc == 2:
    distance_calc()
elif required_calc == 3:
    time_calc()
else:
    print("Invalid selection")
    

