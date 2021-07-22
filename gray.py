# my initial answer
def gray(n):
    out = [0,1]
    i = 1
    while i < n:
        out += [2**i + x for x in out[::-1]]
        i += 1
    return out

# without indexing
def gray2(n):
    out = [0,1]
    for i in range(1,n):
        out += [2**i + x for x in out[::-1]]
    return out

# best submission on leetcode?
def bestgray(n):
    return [i^i>>1 for i in range(2**n)]


def printall(*funcs):
    for func in funcs:
        for i in range(5)[1:]:
            print(f"{i}: {func(i)}")
        print("")

printall(gray, gray2, bestgray)


# 0
# 1

# 00
# 01
# 11
# 10

# 000
# 001
# 011
# 010
# 110
# 111
# 101
# 100

# 0000
# 0001
# 0011
# 0010
# 0110
# 0111
# 0101
# 0100
# 1100
# 1101
# 1111
# 1110
# 1010
# 1011
# 1001
# 1000

# 00000
# 00001
# 00011
# 00010
# 00110
# 00111
# 00101
# 00100
# 01100
# 01101
# 01111
# 01110
# 01010
# 01011
# 01001
# 01000
# 11000
# 11001
# 11011
# 11010
# 11110
# 11111
# 11101
# 11100
# 10100
# 10101
# 10111
# 10110
# 10010
# 10011
# 10001
# 10000