# Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

# Function Description

# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

# sockMerchant has the following parameter(s):

# n: the number of socks in the pile
# ar: the colors of each sock
# Input Format

# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers describing the colors  of the socks in the pile.

# Constraints

#  where
# Output Format

# Return the total number of matching pairs of socks that Alex can sell.

# Sample Input

# 9
# 10 20 20 10 10 30 50 10 20

# Sample Output

# 3

#!/bin/python3

import math
import os
import random
# import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, arr):
    pairs = 0
    dic = {}
    # populate the dictionary with the numbers as keys,
    # and the occurances as values.
    for x in arr:
        dic[x] = 0

    # add 1 to values for each occurance of number
    for x in arr:
        dic[x] += 1

    # add number pairs by flooring the factor of occourances by two.
    for x in dic:
        pairs += math.floor(dic[x] / 2)

    return pairs
