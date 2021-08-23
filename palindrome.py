from _timedPrint import timedPrint

def longestPalindrome(s):
    def recur(s, start, stop):
        # print(s[start:stop+1])
        if not start or stop==len(s)-1:
            return (start,stop)
        if s[start-1]==s[stop+1]:
            return recur(s, start-1, stop+1)
        return (start,stop)

    start, stop = 0, 1
    longest, size = s[0], 1
    while stop < len(s):
        sub = s[start:stop+1]
        # not sure if this check is more efficient in concept (it breaks on even palindromes anyway)
        # if sub[:(len(sub)//2+1)] == sub[len(sub)//2:]:
        if sub == sub[::-1]:
            substart, substop = recur(s,start,stop)
            if substop-substart >= size:
                size = substop-substart
                longest = s[substart:substop+1]
        if start == stop:
            stop += 1
        else:
            start += 1
    return longest


data = ['cbbd', 'jafjsjracecarfjs', 'abcdd']

if __name__ == '__main__':
    timedPrint(data, longestPalindrome)