from _printdriver import printall

# first attempt
# only linearly solves some basic arrays
# needs to iterate through the list differently (from edges to middle maybe?)
# and a more sophisticated area test when encountering new tallLines
def maxArea1(arr):
    if arr[0] < arr[-1]:
        shortLine = arr[0]
        tallLine = arr[-1]
        tallIdx = len(arr) - 1
    else:
        shortLine = arr[-1]
        tallLine = arr[0]
        tallIdx = 0

    area = shortLine * len(arr)

    print(f"shortLine = {shortLine}, tallLine = {tallLine}, tallIdx = {tallIdx}, area = {area}")

    for idx, elem in enumerate(arr[1:], 1):
        print(f"elem {elem} @ idx {idx}: ")

        if elem > shortLine:
            print(f"elem > shortLine")
            areaTest = min(elem, tallLine) * (abs(tallIdx - idx) + 1)
            if areaTest > area:
                print(f"bigger area found: {areaTest}")
                area = areaTest
                if elem > tallLine:
                    print(f"elem {elem} > tallLine")
                    shortLine, tallLine, tallIdx = tallLine, elem, idx
                    print(f"shortLine = {shortLine}, tallLine = {tallLine}, tallIdx = {tallIdx}, area = {area}")
                else:
                    print(f"elem {elem} !> tallLine")
                    shortLine = elem
                    print(f"shortLine = {shortLine}, tallLine = {tallLine}, tallIdx = {tallIdx}, area = {area}")

    print("#########################")
    return area

def maxArea2(arr):
    pass

data = [
    [1,8,6,2,5,4,8,3,7], # 56
    [x for x in range(1,10)], # 25
    [x for x in range(1,10)[::-1]], # 25
    [1,2,9,6,8,3,4,6,7,2,9,0,1] # 81
    ]

printall(data, maxArea1)