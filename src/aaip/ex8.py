# module ex8

"""
Implement a function that takes a list of numbers and returns their
average, and test it with unit tests.
Requirements:
• The function returns the average (mean) of the numbers, or None if the list is
empty.
• The tests are in a separate file test_average.py and use the unittest module.
• At least four tests check
1. the average of a list of positive numbers,
2. the average of a list with negative numbers,
3. the result for an empty list, and
4. the average of a list with a single element.
"""

def calc(numbers):
    if (len(numbers)) == 0:
        return None
    else:
        return (sum(numbers)/len(numbers))
