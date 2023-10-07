import time
import random
from random import randint

def GenerateRandomNumbers():
    random_list = []
    howmany = int(input("How many numbers do you want to have in the list? "))
    for i in range(0, howmany):
        random_list.append(random.randint(0, 5000))
    return random_list


#Quick sorty
def partition(myList, start, end):
    pivot = myList[start]
    left =start+1
    #start outside of the are to be partitioned
    right = end
    done =False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            #swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
        #swap start with my list right
        temp=myList[start]
        myList[start]=myList[right]
        myList[right] = temp
        return right

def quicksort(myList, start, end):
    if start < end:
        #partition the list
        split = partition(myList, start, end)
        #sort both halves
        quicksort(myList, start, split -1)
        quicksort(myList, split + 1, end)
    return myList

myList = GenerateRandomNumbers()
print("this is the list before sorting : ", myList)
sortedList = quicksort(myList,0,len(myList)-1)
theTime = str(time.perf_counter())
print("\n The list after sorting: ", sortedList, "\n and the time taken: ", theTime)