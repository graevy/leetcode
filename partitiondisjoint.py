from _printdriver import *

# initial easy solution?
def disjoint(arr):
    loopindex = 1
    localmaximumindex = 1
    n = arr[0]
    if not n:
        return 1
    for elem in arr[1:]:
        if elem > n:
            n = elem
            localmaximumindex = loopindex
        loopindex += 1
    # print(arr[:localmaximumindex],arr[localmaximumindex:])
    return localmaximumindex
    

data = [[5,0,3,8,6]]
data.append([5,0,3,8,6,1,9,1,10])
data.append([3,4])
data.append([x for x in range(10)])

timed(printall)