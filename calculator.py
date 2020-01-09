"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def get_user_input():

    user_input = input("Calculate here: ")

    return user_input



def user_quit(user_input):

    if user_input[0] == "q":

        return None

    else:

        return user_input

def split_user_input(user_input):

    input_string = user_input.split(" ")

    return input_string


def error_handle(user_input):

    while True:         

        if error_input(user_input): #first fix here

            break

        user_input = incorrect_command(user_input)

        if user_input == None:

            break

def check_digits(user_input):

    for index in range(1,len(user_input)):

        if user_input[index].isdigit() is False:

            print("Enter 2 digits and 1 operator only.")

            return 
        
    return user_input

def incorrect_command(user_input):

    operator_list = ["+", "-", "*", "square", "cube", "pow", "mod", "**", "/", "%", "q"]

    if user_input[0] not in operator_list:

        print("Enter an operator in the beginning of your equation.")

        return 

    else:

        return user_input


def convert_to_int(input_string):

    operator_list = ["+", "-", "*", "square", "cube", "pow", "mod", "**", "/", "%", "q"]

    num_list = []

    for i in input_string:

        if i in operator_list:
            num_list.append(i)

        else:    
            i = int(i)
            num_list.append(i)
            # print(num_list, "print")

    return num_list


def calculator_repl(num_list):

    # for num in input_string:
    # print(input_string)
    if num_list[0] == "+":

        # add(input_string[1][0], input_string[1][1])

        return add(num_list[1], num_list[2])

    elif num_list[0] == "-":

        return subtract(num_list[1], num_list[2])


    elif num_list[0] == "*":

        return multiply(num_list[1], num_list[2])

    elif num_list[0] == "/":

        return divide(num_list[1], num_list[2])

    elif num_list[0] == "**" or num_list[0] == "square":

        return square(num_list[1])

    elif num_list[0] == "**" or num_list[0] == "cube":

        return cube(num_list[1])

    elif num_list[0] == "**" or num_list[0] == "pow":

        return power(num_list[1], num_list[2])

    elif num_list[0] == "%" or num_list[0] == "mod":

        return mod(num_list[1], num_list[2])


def calculator():

    while True:

        user_input = get_user_input()

        user_input = split_user_input(user_input)

        user_input = check_digits(user_input)

        if user_input == None:
            continue


        if_quit = user_quit(user_input)

        if if_quit == None:

            break

        user_input = convert_to_int(user_input)

        solution = calculator_repl(user_input)

        print(solution)

calculator()