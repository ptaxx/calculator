from functions import operation

print("Hello! This is a simple calculator.")
continue_calculation = "y"
user_choice = None

while not user_choice == "e":
    user_choice = input("Use a calculator (c), view history (h) or exit (e)?: ")
    if user_choice == "h":
        with open("history.txt", "r") as history_file:
            print(history_file.read())
        clear_history = input("Clear history (y)?: ")
        if clear_history == "y":
            with open("history.txt", "w") as history_file:
                history_file.write("History:\n")
            print("History cleared.")
            continue
        else:
            continue

    while continue_calculation == "y":
        first_number = None
        operator = None
        second_number = None

        while type(first_number) is not float:
            try:
                first_number = float(input("Enter first number: "))
            except ValueError:
                print("Enter a valid number")

        while operator != "+" and operator != "-" and operator != "/" and operator != "*":
            operator = input("Choose an operator, + - * /: ")
            operator = operator[0]

        print(f"My chosen operator: {operator}")

        while type(second_number) is not float:
            try:
                second_number = float(input("Enter second number: "))
            except ValueError:
                print("Enter a valid number")

        while operator == "/" and second_number == 0:
            try:
                second_number = float(input("Enter another number, cannot divide by zero: "))
            except ValueError:
                print("Enter a valid number")

        operation_result = round(operation(first_number, operator, second_number), 2)

        if first_number.is_integer():
            first_number = int(first_number)
        if second_number.is_integer():
            second_number = int(second_number)
        if operation_result.is_integer():
            operation_result = int(operation_result)

        result: str = f"{first_number} {operator} {second_number} = {operation_result}"
        print(result)
        with open("history.txt", "a") as history_file:
            history_file.write(f"{result}\n")
        print("Do you want to calculate something else?")
        continue_calculation = input("y/n ")

print("Bye!")
