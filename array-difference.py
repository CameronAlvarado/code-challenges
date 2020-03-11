# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b.
# array_diff([1,2],[1]) == [2]

# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]


def array_diff(a, b):
    # loop through array b.
    for i in b:
        # while array a still includes values equal to array b values...
        while i in a:
            # if value is equal, remove it from array a.
            if i in a:
                a.remove(i)
    # return array a
    return a
