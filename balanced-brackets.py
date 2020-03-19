#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'balancedBrackets' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING string as parameter.
#

def balancedBrackets(string):
    # instantaite proper closings
    square = ("[", "]")
    parens = ("(", ")")
    curly = ("{", "}")
    pipe = ("|", "|")
    brackets = ("[", "]", "(", ")", "{", "}", "|")
    booly = True
    # loop through string and check for brackets
    for char in string:
        for char in brackets:
            # if string contains a square bracket
            if square[0] in string:
                # check if there are more than one opening square brackets
                if string.count(square[0]) > 1:
                    # check if there are an odd number of either opening or closing brackets
                    if string.count(square[0]) % 2 is not 0 or string.count(square[1]) % 2 is not 0:
                        return False
                else:
                    booly = True
            # if string contains a parentheses
            if parens[0] in string:
                # check if there are more than one opening curly brackets
                if string.count(parens[0]) > 1:
                    # check if there are an odd number of either opening or closing brackets
                    if string.count(parens[0]) % 2 is not 0 or string.count(parens[1]) % 2 is not 0:
                        return False
                elif string.count(parens[0]) is 1 and string.count(parens[1]) is 0:
                    return False
                else:
                    booly = True
            # if string contains a curly bracket
            if curly[0] in string:
                # check if there are more than one opening curly brackets
                if string.count(curly[0]) > 1:
                    # check if there are an odd number of either opening or closing brackets
                    if string.count(curly[0]) % 2 is not 0 or string.count(curly[1]) % 2 is not 0:
                        return False
                else:
                    booly = True
            # if string contains a pipe[0]
            if pipe[0] in string:
                # if there are more than 2 pipes...
                if string.count(pipe[0]) > 2:
                    for char2 in string:
                        # check if there are more than one opening square brackets
                        if string.count(square[0]) > 1:
                            # if so, check if there are an odd number of square brackets
                            if char2 in square and string.count(char2) % 2 is not 0:
                                return False
                        # check if there are an odd number of parens brackets
                        if char2 in parens and string.count(char2) % 2 is not 0:
                            return False
                        # check if there are an odd number of curly brackets
                        if char2 in curly and string.count(char2) % 2 is not 0:
                            return False
                        # else:
                        #     booly = True
                else:
                    booly = False
            return booly
        else:
            return True


if __name__ == '__main__':
