def add_customer(queue):
    customer = input("What is the customers name?: ")
    queue.append(customer)
    return queue


def main():
    queue = []
    
    while(True):
        add_customer(queue)
        if len(queue) >= 5:
            table_ready = queue[0]
            print(f"{table_ready}'s table is ready\n")
            queue.pop(0)

        print(queue)


if __name__ == "__main__":
    main()



