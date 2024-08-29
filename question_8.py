"""Module containing a program that generates random
4 digits number of 0s and 1s, and then converts the 
generated number to base 10
"""
import random



def rand_num_converter():
    """ function that carries out the convertion and 
     number generation
    """

    rand_list = []
    for i in range(4):
        choice = random.choices([0, 1])
        rand_list.append(choice[0])
    
    binary_string = ""
    for i in rand_list:
        binary_string += str(i)
    base_ten_value = int(binary_string, 2)

    return base_ten_value

print(rand_num_converter())
