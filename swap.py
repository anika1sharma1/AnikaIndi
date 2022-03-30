
def swap1(a, b):
    if a > b:
        b, a = a, b  # swap values
    return a, b  # return 2 values



def swap1_helper(a, b):
    print("Python swap")
    print("Original: ", a, b)
    a, b = swap1(a, b)
    print("After: ", a, b)
    print()
    


def swap2(a, b):
    if a > b:
        swap = a
        a = b
        b = swap
    return a, b


def swap2_helper(a, b):
    print("Classic swap")
    print("Original: ", a, b)
    a, b = swap2(a, b)
    print("After: ", a, b)
    print()



def driver():
    
    swap1_helper(16, 10)
    swap1_helper(10, 16)
    swap1_helper(10.1, 10)
    swap1_helper("def", "abc")
    swap1_helper("abc", "def")
    swap1_helper("ddd", "dd")

7
    swap2_helper(20, 16)
    swap2_helper(16, 20)
    swap2_helper(10.1, 10)
    swap2_helper("def", "abc")
    swap2_helper("abc", "def")
    swap2_helper("ddd", "dd")


if __name__ == "__main__":
    driver()
