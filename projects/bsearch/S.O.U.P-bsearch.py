<SOUP>bsearch.py

'''Team S.O.U.P 
    Parnell Kelley
    Johnathan Curry 
    Jordan Marsaw
    Darius Carter
    Larry Sanders
    Marcus Killebrew'''
    
    
#Parnell Kelley
def bsearch (element, alist):               #Defines the function bsearch for a given list. Accepts the parameter 'element' to search for within the list.
        StartPoint = -1                           #Identifies a starting-point (one boundary) for the function to begin searching the list for the given element.
        EndPoint = len(alist)                     #Identifies an end-point (other boundary) for the function to end its search within the list or given boundaries for the given element.
        while StartPoint != EndPoint-1:           #Initiates a loop for which the condition is that each end/start point and end point/boundaries of the list being searched are not equal to one another. In other words...that the ordered list is not iterating over the same number. 
                MidPoint = (StartPoint + EndPoint) / 2  #Sets the varable 'Midpoint' equal to the average of the start and end points of the ordered list.
                if element > alist[MidPoint]:           #Conditional statement that if the element being searched for is greater than the midpoint of the list/ or if this condition returns the boolean value of True then move within the conditional for the next step. 
                        StartPoint = MidPoint                 #Sets the start point for the list at the midpoint if the given condition returns True.
                elif element < alist[MidPoint]:         #Conditional statement if the previos conditional is false. 
                        EndPoint = MidPoint                   #Sets the End Point equal to the midpoint of the original list if the second condition returns True
                elif element == alist[MidPoint]:        #Conditional statement to be executed if neither of the previos two conditions return True.
                        return MidPoint                       #Exits the function 'bsearch' and returns the value of midpoint after any number of iterations. 
        return -1                                 #if the condition of the loop is not satisfied that startpoint is not equal to endpoint -1 or if no condition within the loop is satisfied then -1 is returned and the function is exited. 


#Johnathan Curry
#I now know that my original submissions were too complicated. I'm a little ashamed it took me this long.

def bsearch(myList, item): #defines the function w/ the perameters
	left = myList[0]   #the lower side of the list is the first element
	right = myList[-1]  #the higher side is the last element 
	midpoint = (left + right) / 2  #the middle of the list is the average of the left and right side
	found = False  #sets up the perameter for the while loop
	while found is False: # I found this is the easiest perameter for the loop, which will continue until the return function
		if item == myList[midpoint]:  #at the start of each iteration, if the item is the same as the midpoint... 
			return myList[midpoint]  #the loop immediatly terminates
		elif item > myList[midpoint]:  #if the item is in the right side of the list...
			midpoint = (midpoint + right) / 2  #the new midpoint is the midpoint of the right side of the list
		elif item < myList[midpoint]:  #shoud the item be in the left side of the list...
			midpoint = midpoint / 2  #the new midpoint is the midpoint of the left side
		else:  #should all else fail...
			return -1  #the loop will terminate and -1 will be shown



#Jordan Marsaw 
def bsearch(L, i):
    return bsearchRecursive(L, i, 0, len(L) - 1)


def bsearchRecursive(L, i, Min, Max):
	''' A recursive solution to binary search. Checks to make sure that list is not empty and if list has elements
	    within the function creates the midpoint and searches through the sorted list for the (i)tem being searched
	    for '''
    if Max < Min:
        return -1
    else:
        Mid = (Min + Max) / 2
        if L[Mid] > i:
            return bsearchRecursive(L, i, Min, Mid - 1)
        elif L[Mid] < i:
            return bsearchRecursive(L, i, Mid + 1, Max)
        else:
            return Mid

  
#Xavier Ward
def Bsearch(SuperList, searchElement): #Fixed
	lowest = 0
    	highest = len(SuperList) - 1
    	mid = (lowest + highest) / 2
    	while highest >= lowest:  
        	if (searchElement >  SuperList[mid]):
        		mid = mid + highest / 2
        	elif searchElement < SuperList[mid]:
        		mid = mid / 2
      		elif searchElement == SuperList[mid]:
        		return mid
      		else:
        		return -1
        		
#Marcus Killebrew    
def binarySearch(BCL , Points): #Final Code
	low = 0 
	high = len(BCL) - 1
	while low <= high:
		middle = (low+high)/2
        if BCL[middle] < Points:
        	low =middle + 1
        if BCL[middle]== Points:
        	return middle
        elif Points <BCL[middle]:
        	high = middle - 1
        else:
        	return middle
        	return -1
       

        		
        		
        		
        		
        		
        		
        		
        		
        		
        		
        		
        		
