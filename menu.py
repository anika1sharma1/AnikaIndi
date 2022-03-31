"""
Introduction to Console Programming
Writing a function to print a menu
"""


# Menu options in print statement
def print_menu1():
    print('0 -- Exit' ) 
    print('1 -- Tree' )
    print('2 -- Matrix' )
    print('3 -- Fibonacci' )
    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Tree',
    2: 'Matrix',
    3: 'Listy',
    4: 'Exit',
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()



# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            if option == 1:
                gen_tree(rows)
            elif option == 2:
                print_matrix3(matrix)
            elif option == 3:
                fibonacci()
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