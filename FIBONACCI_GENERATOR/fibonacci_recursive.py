#!/usr/bin/env python
"""FIBONACCI GENERATOR"""


def fibonacci_recursive(n):
    """ This function calculates the Fibonacci number at a
        specified index using a recursive approach.
    """

    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)  # recursion


if __name__ == "__main__":
    print("FIBONACCI GENERATOR\n")

    mes = f"The Fibonacci series is a sequence where each number is the sum "\
        f"of the two preceding numbers, defined by a mathematical recurrence "\
        f"relationship. Examples; 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...\n"

    print(mes)

    mes2 = f"Indicate which fibonacci number you want, "\
        f"ie; if you want the 2nd indicate '2'\n"

    print(mes2)

    n = int(input("Fibonacci number: "))

    if n < 0:
        print("Please enter a positive integer")
    else:
        print(f"Fibonacci number {n} is: {fibonacci_recursive(n)}")