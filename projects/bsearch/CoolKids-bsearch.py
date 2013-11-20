Group Members


Dontrell Knighten
Glenisha Smith
Travon Speller
Jabari Olatunji
Oluwatoorese Lasebikan
Christian Quist


Solutions:


# def bSearch(searchList, target):
#    low = 0
#    high = len(searchList)
#    while low <= high:
#       if len(searchList)==0:
#          return "EMPTY LIST"
#       testpos = low + (high-low)/2
#       ITEM = searchList[testpos]
#       if ITEM == target:
#          return testpos            
#       elif ITEM < target: 
#          low = testpos+1
#       else:
#          high = testpos-1
#Glenisha Smith @02679391
def bsearch(myList, myItem):
	low = 0 #beginning of list
	high = len(myList)-1 #end of list "-1" is needed or you can run into "index out of range" error
	while low <= high: 
		mid = (low + high)//2 #mid is the index of half way position in your list
		if myList[mid]== myItem: #checks if the item is  located at middle index
			return mid # exits the while loop and returns index of item
		elif myList[mid] < myItem: 
			low = mid + 1 # the mid object is less than the item, the new low becomes 1 index higher
		else :
			high = mid - 1 #if mid is > item the high index bcomes the mid index minus 1
	return -1 #returns -1 if object is not in the list



	


#Oluwatoorese S Lasebikan
#@02720942
#SYCS group assignment
#Binary Search assignment

def bsearch (myList, myItem):
    start = 0
    end = len(myList) - 1
    while start <= end:
        mid = (start + end)/2
    if mid == myItem:
        return mid
    elif x < mid:
        end = mid - 1
    else:
        start = mid + 1
    return -1

