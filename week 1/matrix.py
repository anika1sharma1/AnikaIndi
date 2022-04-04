
def print_matrix3(matrix):
    print("For loop with shortcut (*) row expansion")
    for row in matrix:
        print(*row)


def matrix_driver():
    # setup some text matrices
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [" ", 0, " "]]

    keyboard = [["`", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "-", "="],
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"],
                ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

    numbers = [[0, 1],
               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]]

    # pack into a list of matrices with titles
    matrices = [["Keypad", keypad], ["Keyboard", keyboard], ["Number Systems", numbers]]

    # print each matrix using defined functions
    for title, matrix in matrices:  # unpack matrix with title
        print(title, len(matrix), "x", "~" + str(len(matrix[0])))  # formatted message with concatenation
        #print_matrix1(matrix)
       # print_matrix2(matrix)
        print_matrix3(matrix)
        print()


# tester section
if __name__ == "__main__":
    driver()
