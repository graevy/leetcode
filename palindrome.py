# my first solution. mediocre. i think it's O(nlogn)? my second lc solution
def longestPalindrome(s):
    def recur(s, start, stop):
        if not start or stop==len(s)-1:
            return (start,stop)
        if s[start-1]==s[stop+1]:
            return recur(s, start-1, stop+1)
        return (start,stop)

    start, stop = 0, 1
    longest, size = s[0], 1
    while stop < len(s):
        sub = s[start:stop+1]
        # determines if substring is a palindrome (double negative integer division rounds up)
        # this check fails on even palindromes
        # if sub[:(len(sub)//2)] == sub[-(-len(sub)//2):]:
        if sub == sub[::-1]:
            substart, substop = recur(s,start,stop)
            if substop-substart >= size:
                size = 1+substop-substart
                longest = s[substart:substop+1]
                print(f"new drome {longest} is {size} long")
        if start == stop:
            stop += 1
        else:
            start += 1
    return longest

# this is a famous problem. Manacher's algorithm solves it in LINEAR TIME

print(longestPalindrome('cbbd'))
print(longestPalindrome("aba"))
print(longestPalindrome('abbabbax'))
print(longestPalindrome('JUNKDATAracecarJUNKDATA'))