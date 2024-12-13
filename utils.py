'''
This is a shared module that will handle functions that may be shared across modules

Function:
1. clear_terminal: this clears the terminal to improve readability

'''


import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')