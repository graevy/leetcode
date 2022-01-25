from _timed import timed

@timed
# first try! i'm getting better
def twoSum(arr, n):
    d = {elem:idx for idx,elem in enumerate(arr)}
    for idx,elem in enumerate(arr):
        if n-elem in d:
            return sorted([d[n-elem],idx])

twoSum([5,3,1,7], 8)
twoSum([5,3,1,7], 4)
