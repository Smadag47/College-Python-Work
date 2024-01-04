def input_validation(prompt):
    '''Validate the input given by the user'''
    # Keep running the function until a value is returned
    while(True):
        # Try to receive an integer from the user
        try:
            number = int(input(prompt))
        # If user input is not an integer, print a warning
        except:
            print("wrong input")
        else:
            #Return the number if it is between 0 and 5
            if number >=0 and number <=5:
                print(f"the correct number is {number}")
                return number
            else:
                print("wrong try again")    


def find_maximum(list):
    '''Find the largest value in a gSundayiven list'''
    max_value = list[0]
    for item in list:
        if item > max_value:
            max_value = item
    print(max_value)
    return max_value


def find_minimum(list):
    '''Find the smallest value in a given list'''
    min_value = list[0]
    for item in list:
        if item < min_value:
            min_value = item
    print(min_value)
    return min_value


def count_occurrences(list):
    '''Count how many times a value appears in a list'''
    search_number = int(input("enter a number you want to count: "))
    count = 0
    for item in list:
        if item == search_number:
            count += 1
    print(count)
    return count


def search(list):
    '''Search a list for a given value'''
    search_number = int(input("enter the number you want to search for: "))
    for i in range(len(list)):
        if list[i] == search_number:
            return i
    return -1
    

def sort_algorithm(list):
    '''Sort a list from smallest to largest'''
    list_length = len(list)

    for i in range(list_length - 1):
        swap_count = 0

        for j in range(list_length - 1):

            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swap_count = 1

        if swap_count == 0:
            return list
            break


def main():
    nombre = input_validation("enter a number: ")
    # number_list = [5, 6, 3, 34, 34, 34, 34, 954, 9]
    # # find_maximum(number_list)
    # # find_minimum(number_list)
    # # count_occurrences(number_list)
    # # print(search(number_list))
    # print(sort_algorithm(number_list))

if __name__ == "__main__":
    main()
