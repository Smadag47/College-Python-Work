number_input = input("Enter a number: ")
number_input = int(number_input)

remainder = number_input % 10

match (remainder):
    case 1:
        print(f"{number_input}st")
    case 2:
       print(f"{number_input}nd")
    case 3:
       print(f"{number_input}rd")
    case _:
        print(f"{number_input}th")