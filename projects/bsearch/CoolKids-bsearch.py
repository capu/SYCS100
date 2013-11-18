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
def bsearch(myItem, myList):
	found = False
	low = 0
	high = len(myList)-1
	while low <= high:
		mid = (low + high)//2
		if myList[mid]== myItem:
			found = True
			return mid
		elif myList[mid] < myItem:
			low = mid + 1
		else :
			high = mid - 1
	return -1

