# ---------------------------------------------------------------------------------------
# The following code demonstrates the implementation of the extended Euclidean Algorithm
#
# Parameters :
# -----------
#   - User Input: integer "a"  
#                 non negative integer "b" 
#       requirement: a > b 
#
#   - User Output: gcd(a,b)
#                  integer "x"
#                  integer "y"
#       requirement: gcd(a,b)=1
#                    ax + by = gcd(a,b)
# ---------------------------------------------------------------------------------------

import math

""" This function takes the user input parameter of 'a' and 'b' """
def user_input():
    a = input("Enter the modulus: ")
    b = input("Enter the divider: ")
    return [a, b]


def extended_euclidean(a, b):
    x = 0
    y = 1
    i = 0
    remainder, quotient = euclidean(a, b)
    modulus_divider = []
    modulus_divider.append(b)
    modulus_divider.append(remainder)
    gcd_value = math.gcd(a, b)
    if (gcd_value != 1):
        print("gcd({},{}) = {}".format(a, b, gcd_value))
        print("{}mod{} dont have a modular inverse since gcd({},{})={}".format(b, a, a, b, gcd_value))
    else:
        while remainder != 0:           
            t = x - (y * quotient)
            remainder, quotient = euclidean(modulus_divider[0], modulus_divider[1])
            modulus_divider.pop(0)
            modulus_divider.append(remainder)
            x = y
            y = t 
        t = x - (y * quotient) 
        print("***")
        print("gcd({},{}) = {}".format(a, b, gcd_value))
        print("x = {} and y = {}".format(y, t))




                

    


def euclidean(a, b):
    remainder = a % b
    quotient = a // b
    return remainder, quotient


def main():
    parameters = user_input()
    a = int(parameters[0])
    b = int(parameters[1])
    print(euclidean(a, b))
    extended_euclidean(a, b)
    





if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
