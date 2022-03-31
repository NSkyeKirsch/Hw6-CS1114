"""
Author: Noa Kirschbaum
Assignment / Part: HW6 - Q1
Date due: 2022-03-31
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

def print_shifted_triangle(height, margin, symbol):
    """
    :param height: number of lines triangle will have
    :param margin: margin in front of triangle
    :param symbol: the chosen character
    :return: print triangle
    """
    orig_margin = margin
    final_str = ""
    final_margin = ""
    rows = 1
    while rows <= height*2:
        for m in range(margin + height - 1):
            final_margin += " "
        for i in range(1,rows+1):
            final_str += symbol
        if(len(final_str)%2 != 0):
            print(final_margin + final_str)
            if margin + height > orig_margin:
                margin -= 1
        rows += 1
        final_str = ""
        final_margin = ""




def print_pine_tree(levels, symbol):
    """
    :param levels: number of triangles of increasing sizes
    :param symbol: the character
    :return: big pine tree using print_shifted_triangle
    """
    x = levels - 1
    for i in range(2,levels+2):
        print_shifted_triangle(i,x,symbol)
        x -= 1


def main():
    """""
    test code here
    """""

    input_num_trees = int(input("Enter a positive, non-zero, integer: "))
    input_character = input("Enter a non-whitespace, non-alphanumeric character: ")

    if input_num_trees >= 0 and not input_character.isalnum():
        print_pine_tree(input_num_trees,input_character)

if __name__ == "__main__":
    main();