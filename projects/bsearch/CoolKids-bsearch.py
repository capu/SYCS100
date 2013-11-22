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

#Dontrell Knighten @02671846
def bsearch(array, x): #function for binary search
    first = 0 #first element in list
    last = len(array) - 1 #last element in list
    midpoint = (first + last) / 2 # middle of list
    searching = (first <= last) #boolean value to check where in list you are
    found = False #boolean varialbe to see if item is found or not
    while(searching and not found): #while still searching and item is not found
     midpoint = (first + last) / 2 #middle of list 
     if(x == array[midpoint]): #if value entered is same as value looking for 
        found = True #found is true
        return midpoint #return index of element
     elif( x < array[midpoint]): #else if value is less than midpoint check bottom half of list
        last = midpoint - 1 #set last value equal to the midpoint - 1 
        searching = (first <= last) #still searching
        found = False #item not found 
     else: #else value is in upper half of list
        first = midpoint + 1 #set first value equal to midpoint + 1
        searching = (first <= last) #still searching 
        found = False #item not found
    if(found == False): #if after all searches item not found 
        return -1 #return - 1

	



