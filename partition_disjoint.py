from _timed import batch


# first successful solution
# linear but still kinda slow
def disjoint4(arr):
    minimum = arr[0]
    # leftMaximum is the biggest value in the current candidate output array,
    # i.e. the biggest value to the left of the minimum
    leftMaximum = arr[0]
    # arrMaximum is just the biggest value seen so far
    arrMaximum = arr[0]
    splitIdx = 0
    for idx, elem in enumerate(arr[1:], 1):
        if elem > arrMaximum:
            arrMaximum = elem
            continue
        if elem < minimum:
            minimum = elem
            splitIdx = idx
            leftMaximum = arrMaximum
            continue
        if elem < leftMaximum:
            splitIdx = idx
            leftMaximum = arrMaximum
    return splitIdx+1

# i wasn't really sure if enumerate(arr[1:]) was good practice
def disjoint5(arr):
    gen = enumerate(arr)
    splitIdx, minimum = next(gen)
    leftMaximum = minimum
    arrMaximum = minimum

    for idx, elem in gen:
        if elem > arrMaximum:
            arrMaximum = elem
            continue
        if elem < minimum:
            minimum = elem
            splitIdx = idx
            leftMaximum = arrMaximum
            continue
        if elem < leftMaximum:
            splitIdx = idx
            leftMaximum = arrMaximum
    
    return splitIdx+1

data = [
    [5,0,3,8,6],
    [5,0,3,8,6,1,9,1,10],
    [3,4],
    [x for x in range(1,10)],
    [1,1,1,0,6,12,13,14],
    [0,0,0,1,3,2,3,4],
    [29,33,6,4,42,0,10,22,62,16,46,75,100,67,70,74,87,69,73,88]
]

if __name__ == '__main__':
    batch(data, disjoint4, disjoint5)


# # initial "solution"
# # fails arrays that constantly increase toward the end
# def disjoint1(arr):
#     loopindex = 1
#     localmaximumindex = 1
#     n = arr[0]
#     if not n:
#         return 1
#     for elem in arr[1:]:
#         if elem > n:
#             n = elem
#             localmaximumindex = loopindex
#         loopindex += 1
#     # print(arr[:localmaximumindex],arr[localmaximumindex:])
#     return localmaximumindex

# # it's not so easy
# def disjoint2(arr):
#     return arr.index(min(arr))+1

# # fails on final datapoint
# def disjoint3(arr):
#     minimum = arr[0]
#     minimumIndex = 0
#     # basically min(arr), but also save the minimum's index to save an unnecessary loop
#     for idx, elem in enumerate(arr[1:], 1):
#         if elem < minimum:
#             minimum = elem
#             minimumIndex = idx

#     greatestNumberBeforeMinimum = minimum
#     for elem in arr[:minimumIndex]:
#         if elem > greatestNumberBeforeMinimum:
#             greatestNumberBeforeMinimum = elem

#     returnidx = 0
#     for idx, elem in enumerate(arr[minimumIndex:], minimumIndex):
#         if elem < greatestNumberBeforeMinimum:
#             returnidx = idx

#     return returnidx+1