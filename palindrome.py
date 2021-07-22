def longestPalindrome(s):
    def recur(s, start, stop):
        print(s[start:stop+1])
        if not start or stop==len(s)-1:
            return (start,stop)
        if s[start-1]==s[stop+1]:
            return recur(s, start-1, stop+1)
        return (start,stop)

    start, stop = 0, 1
    longest, size = s[0], 1
    while stop < len(s):
        print(start,stop)
        sub = s[start:stop+1]
        if sub[:(len(sub)//2)] == sub[len(sub)//2:]:
            substart, substop = recur(s,start,stop)
            if substop-substart > size:
                size = substop-substart
                longest = s[substart:substop+1]
        if start == stop:
            stop += 1
        else:
            start += 1
    return longest

print(longestPalindrome('cbbd'))