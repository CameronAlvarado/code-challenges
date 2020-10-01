def AND(a, b):
    if a is b:
        return a
    else:
        return 0


def OR(a, b):
    if a is b:
        return a
    else:
        return 1


def NOT(a):
    if a is 1:
        return 0
    else:
        return 1


def XOR(a, b):
    x = AND(a, b)
    y = NOT(x)
    z = OR(a, b)
    i = AND(y, z)
    return i


def HADD(a, b):
    x = XOR(a, b)
    y = AND(b, a)
    # (sum, carry)
    return [x, y]


def FADD(a, b, c):  # full adder
    x = HADD(a, b)
    sum = x[0]
    carry = x[1]

    y = HADD(sum, c)
    sum = y[0]
    carry2 = y[1]

    carry3 = OR(carry, carry2)

    return [carry3, sum]


# TODO
# Create an 8-bit adder.
print(HADD(0, 0))
