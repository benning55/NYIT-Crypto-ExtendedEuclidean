# Group9: Cryptography Fall 2024

# Extended Euclidean Algorithm Implementation

## Overview

This project implements the Extended Euclidean Algorithm in Python. The algorithm is a powerful tool in number theory and cryptography, used to find the greatest common divisor (GCD) of two numbers and express it as a linear combination of these numbers.

## Functionality

The program takes two inputs:
1. An integer `a`, which is the modulus
2. A non-negative integer `b` that is less than `a`

The program outputs three values:
1. `gcd(a,b)`: The greatest common divisor of `a` and `b`
2. Integer `x`
3. Integer `y`

Such that: `ax + by = gcd(a,b)`

## Implementation Details

The Extended Euclidean Algorithm is implemented in Python 3. The main functionality is encapsulated in the `extended_euclidean(a, b)` function, which returns a tuple `(gcd, x, y)`.

### Algorithm Steps:

1. If `b` is 0, return `(a, 1, 0)` as `a` is the GCD, and 1*a + 0*b = a
2. Recursively call the function with `b` and `a % b`
3. Update `x` and `y` based on the recursive call results

## Usage

To run the program:

1. Ensure you have Python 3 installed on your system.
2. Clone this repository.
3. Navigate to the project directory.
4. Run the following command:
5. Follow the prompts to enter values for `a` and `b`.

## Docker Support

A Dockerfile is provided to containerize the application. To use it:

1. Build the Docker image; `docker build -t <image-name> .`
2. Run the container; `docker run -e a=17 -e b=1 <image-name>`

## Example

Input:
- a = 48
- b = 18

Output:
- GCD(48, 18) = 6
- x = -1
- y = 3

Verification: 48 * (-1) + 18 * 3 = 6

## Note

This implementation assumes that the input `b` is non-negative and less than `a`. The program includes input validation to ensure these conditions are met.

