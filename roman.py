def romanToNum(string):

    # init all romans
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # init out num
    num = 0

    # convert input to list

    # iterate over the list
    for index, i in enumerate(string):

        # evaluate the numerals
        num = num + romans[i]
        # num += romans[i]

    # add values to num

    if index > 0:

        # check whether the len of the input is > 0

        # return num
    return num


print(romanToNum("X"))
