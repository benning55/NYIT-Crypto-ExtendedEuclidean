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
import os

""" This function takes the user input parameter of 'a' and 'b'"""
def user_input():
    # Try to get values from environment variables
    a = os.environ.get('MODULUS')
    b = os.environ.get('DIVIDER')
    # Check if both variables are set
    if a is None or b is None:
        raise ValueError("Both MODULUS and DIVIDER must be set as environment variables")
    try:
        # Convert to integers
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError("MODULUS and DIVIDER must be valid integers")
    if b <= 0:
        raise ValueError("DIVIDER must be a positive integer")
    return [a, b]

"""This outputs the x and y and gcd(a, b)"""
def extended_euclidean(a, b):
    x = 0
    y = 1
    x_values = [1,0]
    y_values = [0,1]

    remainder, quotient = euclidean(a, b)
    modulus_divider = []
    modulus_divider.append(b)
    modulus_divider.append(remainder)
    gcd_value = math.gcd(a, b)
    # the follwing condition checks if 'a' and 'b' are co-prime
    if (gcd_value != 1):
        print("gcd({},{}) = {}".format(a, b, gcd_value))
        print("{}mod{} dont have a modular inverse since gcd({},{})={}".format(b, a, a, b, gcd_value))
        print("The values are not co-prime")
    # the following calculate the remainder and 'x' 'y' values
    else:
        while remainder != 0:           
            x = x_values[0] - (x_values[1]*quotient)
            x_values.pop(0)
            x_values.append(x)
            y = y_values[0] - (y_values[1]*quotient)
            y_values.pop(0)
            y_values.append(y)
            remainder, quotient = euclidean(modulus_divider[0], modulus_divider[1])
            modulus_divider.pop(0)
            modulus_divider.append(remainder)
        # corrects the value of 'y' when  it's negative
        while (y < 0):
            y = y+a
            x = x-b
  
        results = (x*a) + (y*b)
        print("***")
        print("gcd({},{}) = {}".format(a, b, gcd_value))
        print("x = {} and y = {}".format(x, y))
        print("the formula ax + by= {}".format(results))
        print("the modular inverse of {} mod {} = {}".format(b, a, y))


"""This function calculates the remainder and quotient"""
def euclidean(a, b):
    remainder = a % b
    quotient = a // b
    return remainder, quotient


"""This function takes the user input and outputs 'x' 'y' 'gcd(a,b)' """
def main():
    parameters = user_input()
    a = int(parameters[0])
    b = int(parameters[1])
    extended_euclidean(a, b)
    

if __name__ == '__main__':
    # execute only if run as the entry point into the program 
    main()