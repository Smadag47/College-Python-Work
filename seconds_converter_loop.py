def minutes_to_seconds():
    '''Ask user for a number of minutes and convert them into seconds'''
    try:
        minutes = int(input("Enter the number of minutes: "))
        seconds = minutes * 60
        print(f"{minutes} minutes is equivelent to {seconds} seconds")
    except ValueError:
        print("invalid input")


def hours_to_minutes():
    '''Ask user for a number of hours and convert them into minutes'''
    try:
        hours = int(input("Enter the number of hours: "))
        minutes = hours * 60
        print(f"{hours} hours is equivelent to {minutes} minutes")
    except ValueError:
        print("Invalid input")


def days_to_hours():
    '''Ask user for a number of days and convert them into hours'''
    try:
        days = int(input("Enter the number of days: "))
        hours = days * 24
        print(f"{days} days is equivelent to {hours} hours")
    except ValueError:
        print("invalid input")


def menu():
    '''Display a menu to display the options to the user'''
    print("-" * 50)
    print('''
    Please select an option
    1. Convert minutes to seconds
    2. Convert hours to minutes
    3. Convert days to hours
    4. Exit      
    ''')
    print("-" * 50)


def main():
    
    finished = False

    menu()

    while not finished:
        # Ask the user to select which conversion they want
        try:
            user_choice = int(input("Please enter your choice: "))
        except ValueError:
            print("select again")
        
        match(user_choice):
            case(1):
                minutes_to_seconds()
            case(2):
                hours_to_minutes()
            case(3):
                days_to_hours()
            case(4):
                finished = True
            case _:
                print("invalid input")
        
    input("Press any key to exit ")

if __name__ == "__main__":
    main()



    