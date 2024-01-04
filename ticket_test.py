def get_ticket_sales(days, ticket_sales):
    for day in days:
        sales = float(input(f'Enter the sales for {day}'))
        ticket_sales.append(sales)


def average_ticket_sales(days, ticket_sales):
    average_sales = sum(ticket_sales) / len(days)
    return average_sales


def highest_number(ticket_sales):
    '''Find the largest value in a list'''
    max_value = ticket_sales[0]
    for item in ticket_sales:
        if item > max_value:
            max_value = item
    print(max_value)
    return max_value


def lowest_number(ticket_sales):
    '''Find the smallest value in a given ticket_sales'''
    min_value = ticket_sales[0]
    index = 0
    for item in ticket_sales:
        if item < min_value:
            min_value = item
        else:
            index += 1
    print(min_value)
    return min_value


def main():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ticket_sales = []
    get_ticket_sales(days, ticket_sales)
    highest_sales = highest_number(ticket_sales)
    lowest_sales = lowest_number(ticket_sales)
    print (f'The highest sales was {highest_sales}. The lowest sales was {lowest_sales}')

if __name__ == '__main__':
    main()
