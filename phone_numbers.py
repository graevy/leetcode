# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# 2:[a,b,c], 3:[d,e,f], 4:[g,h,i], 5:[j,k,l], 6:[m,n,o], 7:[p,q,r,s], 8:[t,u,v], 9:[w,x,y,z]

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:

# Input: digits = ""
# Output: []

# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

 

# Constraints:

#     0 <= digits.length <= 4
#     digits[i] is a digit in the range ['2', '9'].

def phone_number_combos(digits):
    if not digits:
        return []

    def chr_fn(digit: str):
        match digit:
            case '7':
                return ['p','q','r','s']
            case '8':
                return ['t','u','v']
            case '9':
                return ['w','x','y','z']
            case _:
                return [chr(int(digit)*3 + i + 91) for i in range(3)]

    def recur(arr,combo=""):
        if not arr:
            result.append(combo)
        else:
            for val in arr[0]:
                recur(arr[1:], combo + val)

    letters = [chr_fn(digit) for digit in digits]
    result = []

    recur(letters)

    return result

print(phone_number_combos('257'))