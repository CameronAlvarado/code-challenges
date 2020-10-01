def is_prime(num):
    # check for edge case
    if num < 2:
        return False
    # loop though numbers up to value of num
    for x in range(2, num - 1):
        # divide num by each number
        # if a result equals an integer
        # return false
        if (num % x) == 0:
            return False
            break
    # default to returning true
    else:
        return True
