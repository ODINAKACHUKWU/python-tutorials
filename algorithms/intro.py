"""Module demonstrating the concept of algorithm analysis"""

import time

# ANALYZING ALGORITHM PERFORMANCE:

# APPROACH 1: Measuring algorithm execution time
# Limitation: This approach is not always reliable since
# time measurements can be affected by various factors (e.g., system's processing
# power, programming language etc).
start_time = time.time()

for i in range(1, 6):
    print(i)

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")

# APPROACH 2: Counting algorithmic steps
# Limitation: This approach is not also reliable because, among other reasons, it may not be
# easy to determine the exact number of steps an algorithm takes depending on its structure
# and complexity.
# Example 1:
# This program takes 5 steps to complete (it goes through a loop 5x and prints `i` each time).
# Therefore, f(n) = 5;
# We can derive an equation for the total number of steps:
#   `f(n) = n`; where n is the number of iterations.
for i in range(1, 6):
    print(f"Test iteration {i}")  # 5 steps (prints 1 to 5)

# Example 2:
# This program takes 11 steps to complete (it assigns the variable count to zero, goes through
# a loop 5x and prints `i` each time, and increments `COUNTER` 5x - by 1 each time).
# We can derive an equation for the total number of steps:
#   f(n) = 1 + 2n; where n is the number of iterations, 2 is the 2 steps in the loop, and 1 is
#                  the 1 step in the assignment.
# Therefore, f(n) = 1 + 2 * 5 = 11
COUNTER = 0  # 1 step
for i in range(1, 6):
    print(f"Test iteration {i}")  # 5 steps (prints 1 to 5)
    COUNTER += 1  # 5 steps (increments COUNTER)

# NOTES:
# - The variable `n` is referred to as the `size of the problem` or `input size`.
# - We can say that the time (T) it takes to solve a problem of size `n` equals f(n) and can be
#   represented mathematically as T(n) = f(n) = n | 1 + 2n (the 2 examples above).

# Example 3:
# This program takes T(n) = n + n³ steps to complete (it goes through the first loop n times, and
# for the second loop, it goes through another loop n times, and for each iteration of that loop,
# it goes through yet another loop n times).


def print_it(n):
    """Function to print iterations"""
    for j in range(n):  # T(n) = n
        print(j)

    for x in range(n):  # T(n) = n³
        print(x)
        for y in range(n):
            print(y)
            for z in range(n):
                print(z)


# APPROACH 3: Using Big O Notation
# This approach focuses on the most important/impactful order (O) in an algorithm which is what
# we care about the most. This concept describes the `worst-case scenario`. It focuses on the
# `dominant term (highest order term)` and ignores lower-order terms and constant factors - O(1).
# Using Example 3:
# The first loop contributes O(n) (Linear time) in the order of magnitude and the second loop
# contributes O(n³) (Cubic time), so the overall complexity is O(n + n³) = O(n³).
