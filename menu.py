"""
Introduction to Console Programming
Writing a function to print a menu
"""

import sys
sys.path.insert(1, 'week 1')
sys.path.insert(1, 'week 2')
sys.path.insert(1, 'week 3')


from matrix import print_matrix3, matrix_driver
from tree import gen_tree, tree_driver
from fibonacci import fibonacci
from factoria import factorial, factorial_driver

# Menu options in print statement
def print_menu1():
    print('0 -- Exit' ) 
    print('1 -- Tree' )
    print('2 -- Matrix' )
    print('3 -- Fibonacci' )
    print('4 -- Factorial' )
    runOptions()


# Menu options as a dictionary
menu_options = {
    0: 'Exit',
    1: 'Tree',
    2: 'Matrix',
    3: 'Fibonacci',
    4: 'Factorial'
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, u'\u001b[34m--\u001b[0m', menu_options[key] )
    runOptions()


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input(u'\u001b[34mEnter your choice 1-4: \u001b[0m'))
            if option == 1:
                tree_driver()
            elif option == 2:
                matrix_driver()
            elif option == 3:
                fibonacci()
            elif option == 4:
                factorial_driver(factorial)
            # Exit menu    
            elif option == 0:  
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
  print_menu2()
  