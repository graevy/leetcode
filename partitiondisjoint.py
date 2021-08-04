from _printdriver import printall,timed

# initial easy solution?
# fails arrays that constantly increase toward the end
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

# sloppy demonstration of why the algorithm isn't easy?
# (index method is an unnecessary array loop)
def disjoint2(arr):
    return arr.index(min(arr))+1

# fails on final datapoint
def disjoint3(arr):
    minimum = arr[0]
    minimumIndex = 0
    # basically min(arr), but also save the minimum's index to save an unnecessary loop
    for idx, elem in enumerate(arr[1:], 1):
        if elem < minimum:
            minimum = elem
            minimumIndex = idx

    greatestNumberBeforeMinimum = minimum
    for elem in arr[:minimumIndex]:
        if elem > greatestNumberBeforeMinimum:
            greatestNumberBeforeMinimum = elem

    returnidx = 0
    for idx, elem in enumerate(arr[minimumIndex:], minimumIndex):
        if elem < greatestNumberBeforeMinimum:
            returnidx = idx

    return returnidx+1

def disjoint4(arr):
    pass

data = [[5,0,3,8,6]]
data.append([5,0,3,8,6,1,9,1,10])
data.append([3,4])
data.append([x for x in range(1,10)])
data.append([1,1,1,0,6,12,13,14])
data.append([0,0,0,1,3,2,3,4])
data.append([29,33,6,4,42,0,10,22,62,16,46,75,100,67,70,74,87,69,73,88])

printall(data, disjoint, disjoint2, disjoint3)
# timed(printall)