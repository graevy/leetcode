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
def max_area_1(arr):
    if arr[0] < arr[-1]:
        shortLine = arr[0]
        tallLine = arr[-1]
        tallIdx = len(arr) - 1
    else:
        shortLine = arr[-1]
        tallLine = arr[0]
        tallIdx = 0

    area = shortLine * len(arr)

    for idx, elem in enumerate(arr[1:], 1):
        if elem > shortLine:
            areaTest = min(elem, tallLine) * (abs(tallIdx - idx) + 1)
            if areaTest > area:
                area = areaTest
                if elem > tallLine:
                    shortLine, tallLine, tallIdx = tallLine, elem, idx
                else:
                    shortLine = elem
    return area

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

# i slightly fine-tuned the bruteforce. 50% fewer total comparisons
def max_area_3(arr):
    largest = 0
    n = len(arr)
    for idx_i in range(n):
        for idx_j in range(idx_i):
            if calc_area(arr,idx_i,idx_j) > largest:
                largest = calc_area(arr,idx_i,idx_j)
    return largest


# finally some progress. this passed all test cases in linear time.
# by weighting each value, relative comparisons don't need to be made
# unfortunately, an array with a single massive value will result in the same value for left and right
# the array [1,2,1] defeats this algorithm because both sides select the middle value
# simply preventing both sides from selecting the same value results in an area of 1 instead of 2
def max_area_4(arr):
    n = len(arr)
    right = max([(item * idx, item, idx) for idx,item in enumerate(arr)])
    left = max([(item * (n-idx), item, idx) for idx,item in enumerate(arr)])
    height = min(right[1], left[1])
    width = abs(right[2] - left[2])
    return height * width


# ultimately, all weighting schemes i could come up with were defeatable
# the best solution is to examine widths instead of heights
def max_area_5(arr):
    max_width = len(arr) - 1
    left, right = 0, max_width
    area = 0
    # decrement widths as necessary until we've traversed the whole array
    for width in range(max_width, 0, -1):
        if arr[left] < arr[right]:
            area, left = max(area, arr[left] * width), left + 1
        else:
            area, right = max(area, arr[right] * width), right - 1
    return area




data = [
    [1,8,6,2,5,4,8,3,7], # 49
    [x for x in range(1,10)], # 20
    [x for x in range(1,10)[::-1]], # 20
    [1,2,9,6,8,3,4,6,7,2,9,0,1], # 72
    [1,2,1]
    ]

_timed.timeBatch(data, max_area_4, max_area_5, loops=10000)
# print(max_area_5(data[-1]))