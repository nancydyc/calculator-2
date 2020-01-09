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


def split_user_input(user_input):

    input_string = user_input.split(" ")

    return input_string

def convert_to_int(input_string):
    for i in input_string:
        i = int(i)
        print(input_string)

        return input_string

def calculator_repl(input_string):

    # for num in input_string:

    if input_string[0] == "+":

        add(int(input_string[1], input_string[2]))


def calculator():

    while True:

        user_input = get_user_input()

        user_input = split_user_input(user_input)

        user_quit(user_input)

        user_input = convert_to_int(user_input)

        calculator_repl(user_input)


calculator()