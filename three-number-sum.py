#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'threeNumberSum' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER target
#

def threeNumberSum(arr, target):
    # declare an empty array
    ans = []
    trip = []
    # loop through array to find 3 values
    for a in arr:
        for b in arr:
            for c in arr:
                # check if the 3 values add up to target
                if (a + b + c) is target:
                    # if so, append each element to array with no repeating values
                    if a is not b and a is not c and b is not c:
                        trip = [a, b, c]
                        # sort triplet in ascending order
                        trip.sort()
                        # exclude duplicate triplets
                        if trip not in ans:
                            ans.append(trip)
    print(ans)
    # sort the triplets in the answer
    ans.sort()
    return ans


if __name__ == '__main__':
