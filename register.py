my_class = ["Robin", "Bill", "James", "Mary", "Patricia"]
present_students = []
absent_students = []

for x in my_class:
    present = input(f"Is {x} present? (y/n): ")
    
    if present == "y":
        present_students.append(x)
    elif present == "n":
        absent_students.append(x)

print(sorted(present_students), " are present")
