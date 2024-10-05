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
A Dockerfile is provided to containerize the application. To use it:

1. Build the Docker image; `docker build -t <image-name> .`
2. Run the container; `docker run -e a=<a_value> -e b=<b_value> <image-name>`

## Example

Input:
- a = 13
- b = 7

Docker command to run:
1. `docker build -t cryptography-hw .`
2. `docker run -e a=48 -e b=18 cryptography-hw`

Output:
- GCD(13, 7) = 1
- x = -1
- y = 2
- the formula ax + by= 1
- the modular inverse of 7 mod 13 = 2

## Note

This implementation assumes that the input `b` is non-negative and less than `a`. The program includes input validation to ensure these conditions are met.

