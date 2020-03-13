#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fibonacci' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def fibonacci(n):
    # declare an array
    array = [0, 1]
    # declare am integer
    count = 0
    # for every step up to n minus the two integers in array...
    if n is 1:
        return [0]
    for i in range(n-2):
        # Add last two integers from array to count
        count = array[-2] + array[-1]
        # append the current count to the array
        array.append(count)
    return array


if __name__ == '__main__':
