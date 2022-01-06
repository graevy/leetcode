import _timed


def calc_area(arr, idx_i, idx_j):
    # return (i if i>j else j) * abs(idx_i - idx_j)
    i,j = arr[idx_i],arr[idx_j]
    if i>j:
        return j * abs(idx_i - idx_j)
    else:
        return i * abs(idx_i - idx_j)


# first attempt
# only linearly solves some basic arrays
# needs to iterate through the list differently (from edges to middle maybe?)
# and a more sophisticated area test when encountering new tallLines
# def maxArea1(arr):
#     if arr[0] < arr[-1]:
#         shortLine = arr[0]
#         tallLine = arr[-1]
#         tallIdx = len(arr) - 1
#     else:
#         shortLine = arr[-1]
#         tallLine = arr[0]
#         tallIdx = 0

#     area = shortLine * len(arr)

#     for idx, elem in enumerate(arr[1:], 1):
#         if elem > shortLine:
#             areaTest = min(elem, tallLine) * (abs(tallIdx - idx) + 1)
#             if areaTest > area:
#                 area = areaTest
#                 if elem > tallLine:
#                     shortLine, tallLine, tallIdx = tallLine, elem, idx
#                 else:
#                     shortLine = elem
#     return area

# if you fail, make a brute force algorithm first
def max_area_2(arr):
    largest = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            # saving calc_area is quadratic, running it twice is logarithmic
            if calc_area(arr, i, j) > largest:
                largest = calc_area(arr, i, j)
    return largest

# i slightly fine-tuned the bruteforce
def max_area_3(arr):
    largest = 0
    n = len(arr)
    for idx_i in range(n):
        for idx_j in range(idx_i):
            if calc_area(arr,idx_i,idx_j) > largest:
                largest = calc_area(arr,idx_i,idx_j)
    return largest

def max_area_4(arr):
    n = len(arr)
    values2 = sorted([(item * idx, item, idx) for idx,item in enumerate(arr)], reverse=True)
    values3 = sorted([(item * (n-idx), item, idx) for idx,item in enumerate(arr)], reverse=True)
    height = min(values2[0][1], values3[0][1])
    width = abs(values2[0][2] - values3[0][2])
    return height * width

data = [
    [1,8,6,2,5,4,8,3,7], # 49
    [x for x in range(1,10)], # 20
    [x for x in range(1,10)[::-1]], # 20
    [1,2,9,6,8,3,4,6,7,2,9,0,1] # 72
    ]

_timed.timeBatch(data, max_area_4, loops=10000)
# print(max_area_4(data[0]))