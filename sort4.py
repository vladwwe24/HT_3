from random import randint
import time

timer_1 = time.time()
list = [randint(1, 100) for i in range(100000)]


def insertion_sort(mylist):
    for i in range(1, len(mylist)):
        j = i - 1
        while mylist[j] > mylist[j+1] and j >= 0:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
            j -= 1
    return mylist

b = insertion_sort(list).copy()

timer_2 = time.time()
time_1 = timer_2 - timer_1



timer_3 = time.time()


def selection_sort(mylist):
    for i in range(1, len(mylist)):
        value = mylist[i]
        j = i - 1
        while j >= 0 and mylist[j] > value:
            mylist[j + 1] = mylist[j]
            j = j - 1
        mylist[j + 1] = value
    return list


b = selection_sort(list).copy()


timer_4 = time.time()
time_2 = timer_4 - timer_3

timer_5 = time.time()


def bubble_sort(mylist):
    for z in range(0, len(mylist) - 1):
        for x in range(0, len(mylist) - 1 - z):
            if mylist[x] > mylist[x + 1]:
                mylist[x], mylist[x + 1] = mylist[x + 1], mylist[x]

    return mylist


new_list = bubble_sort(list).copy()


timer_6 = time.time()
time_3 = timer_6 - timer_5


def sort_test(func):
    if func :
        return True
    else :
        return False


print('Insetion sort: time = ',time_1,';the list is sorted correctly =' + str(sort_test(insertion_sort(list))))
print('Selection sort: time = ',time_2,';the list is sorted correctly =' + str(sort_test(selection_sort(list))))
print('Bubble sort: time = ',time_3,';the list is sorted correctly =' + str(sort_test(bubble_sort(list))))
