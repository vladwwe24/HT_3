from random import randint
import time

timer = time.time()

a = [randint(1, 100) for i in range(100000)]
def sort_abs(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1
        while j >= 0 and list[j] > value:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = value
    return list

print(a)
b = sort_abs(a).copy()
print(b)

timer_2 = time.time()
print(timer_2 - timer)