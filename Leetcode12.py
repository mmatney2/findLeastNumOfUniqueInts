def findLeastNumOfUniqueInts(arr, k):

    #Input: arr = [4,3,1,1,3,3,2], k = 3
    #Output: 2
    #2 represents the number of different elements left. 
    # i and j ONLY
    #k is the number of numbers to remove if seen least amount of times
    #HOW TO COUNT THE NUMBERS THAT ARE THE LEAST IN THE ARR
    dict = {}
    count = 0
    for a in arr:
        if a not in dict:
            dict[a] = arr.count(a)
            print(dict)
        count += 1
        for b in arr:
            if arr.count(a)<arr.count(b):
                a.remove(b)
    
        return 


# print(findLeastNumOfUniqueInts([2,2,2,3, 1], 2))
from collections import Counter
def findLeastNumOfUniqueInts(arr, k):
    counter = Counter(arr)
    print(counter)

    t = sorted(counter.items(), key=lambda x: x[1])
    print(t)
    for v, cnt in t:
        if k >= cnt:
            k -= cnt
            counter.pop(v)
        else:
            break
    return len(counter)
print(findLeastNumOfUniqueInts([2,2,2,3, 1, 5, 5, 8, 8], 2))

# f = lambda x: x[1] (2)
# print(f)