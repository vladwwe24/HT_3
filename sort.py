from random import randint
import time

timer = time.time()
list = [randint(1, 100) for i in range(100000)]

def merge_sort(mylist):
    if len(mylist) <= 1:
        return mylist
    middle = int(len(mylist)/2)
    left = merge_sort(mylist[:middle])
    right = merge_sort(mylist[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

print(list)
list_2 = merge_sort(list)
print(list_2)

timer_2 = time.time()
print(timer_2 - timer)