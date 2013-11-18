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
def bsearch(item, myList): #defines the function
	midpoint = len(myList) / 2 #establishes the value of the midpoint
	left = range(0, midpoint) #tells initially what the first half of the list will be
	right = range(midpoint, len(myList)-1) #tells what the second half will be
	while left and right != 0: #establishes the perameters of the loop
		if midpoint == myList[item]: #if the midpoint is equal to the desired element...
			return 1 #it will exit the loop and skip to the end
		elif midpoint < myList[item]: #if the midpoint is less than the desired element...
			midpoint = len(left) / 2 #there will be a new midpoint based on the first half of the list, and the loop will repeat
		elif midpoint > myList[item]: #if the midpoint is greater than the desired element...
			midpoint = len(right) / 2 #there will be a new midpoint based on the second half of the list, and the loop will repeat
		else: #if none of these are satisfied, that means the desired element does not exist
			return -1 #and the program will exit the loop
