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

# def choose_maths(user_input):


#     operator_list = ["+", "-", "*", "square", "cube", "pow", "mod", "**", "/", "%"]
#     if user_input[0] in operator_list:



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

        if_quit = user_quit(user_input)

        if if_quit == None:

            break

        user_input = convert_to_int(user_input)

        solution = calculator_repl(user_input)

        print(solution)

calculator()