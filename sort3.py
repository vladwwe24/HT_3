from random import randint
import time

timer = time.time()
x = [randint(1, 100) for i in range(100000)]
def bubble_sort(mylist):
    for z in range(0,len(mylist)-1):
        for x in range(0,len(mylist)-1-z):
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]

    return mylist
print(x)
new_list = bubble_sort(x).copy()
print(new_list)
new_timer = time.time()
print(new_timer - timer)




