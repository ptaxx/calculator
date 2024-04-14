# def - python inbuilt word that means "definition"

# function definition: blueprint / project of a function

def operation(number1, operation_type, number2):
    if operation_type == "+":
        return float(number1 + number2)
    elif operation_type == "-":
        return float(number1 - number2)
    elif operation_type == "*":
        return float(number1 * number2)
    elif operation_type == "/" and number2 != 0:
        return float(number1 / number2)
    else:
        exit("Something went wrong. Exiting...")



# result = float(plus_operation(2, 2))
# print(result)
