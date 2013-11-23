''' Team r3-Bo0t 
	Barry Harris
	Errol Grannum
	Boluwatife Aiki-Raji
	Hallie Lomax
	Brittany Miller
	Eric Walker 
	Chris Quist'''

##Eric Walker
def bitSearch(listA, s): #defines the function of bitsearch for a given listA and a search value s
    extant = False #sets the parameter in which to run the while loop
    startingPara = 0 #sets the starting parameter at 0
    endingPara = len(listA) - 1 #sets the ending parameter to be the length of the list minus 1, for the purposes of indexing
    search = s #defines search as s
    while ((endingPara >= startingPara) and extant == False): #will run the function until the ending para is less than the starting para + 1 and extant = False
        midpoint = ((startingPara + endingPara) / 2) #the midpoint will be the exact middle between the starting and ending para's sum. Floor division would skew this process
        if search < listA[midpoint]: #checks and sees if the search value is greater than the index of listA midpoint
            endingPara = midpoint - 1 #if so, the ending para will become 1 less than the midpoint
        elif search > listA[midpoint]: #checks to see if the search value is greater than the index of listA at the midpoint
            startingPara = midpoint + 1 #if so, the starting para becomes the midpoint + 1
        elif search == listA[midpoint]: #checks to see if the search value IS the index listA at midpoint
            return search #if so, exits the function, returning the search value to indicate it was found
    else:
        return -1 #if none of the above are true, will return -1



# Chris Quist's binary search
def bsearch(wlist, item):
    beginning=0
    end = len(wlist)
    while beginning!=end:
        middle = (beginning + end)/2
        if item == wlist[ middle]:
            return middle
        elif item < wlist[middle]:
            end = middle
        else:
            if beginning == middle:
                return -1
            else:
                beginning = middle
    return -1

# Errol Grannum's binary search
#MyList = [1,4,10,13,14,15,19,29,36]
#Target = 13
 # iterative implementation
def BinarySearch(MyList,Target):
    low = 0
    high = len(MyList)
    while low < high:
        mid = (low + high)//2
        if Target > MyList[mid]:
            low = mid + 1
        elif Target < MyList[mid]:
            high = mid
        else: 
            return mid
    return -1
#print BinarySearch(MyList,Target)

#Hallie Lomax's Binary Search

# Above is my list
def bsearch(list, b): # Function takes the parameters list and 'b' (the object to find)
   i = 0 # Setting i to zero and search to an empty list
   search = []
   while i < len(list): # creates a list of the numbers associated with the position of each piece of the searchable list
     search.append(i)
     i+=1
   if not list: 
     return -1
   while (not search is False): # Keeps looping until the list is empty
     i = len(search) - 1 # Resets i to being the length of the current list
     if list[search[0]] == b:
       return search[0]
     elif list[search[i]] < b or b < list[search[0]]: # if the thing you're looking for is bigger or smaller than the list that the function is looking at, then its probably not there. So it returns -1 and quits
       return -1
     elif list[search[i]] == b: #if the last position in the list is b, then returns the number at that corresponding position in search
       return search[i]
     else: # if none of the above apply, it'll cut the list in the following way
       i /= 2 #Cuts i in half
       if (i == 0): #if i is zero, then we probably only have one more place to search.
         if list[search[i]] == b:
           return search[0]
         else:
           return -1
       elif list[search[i]] == b: # if the list search at i is b, then we return search position i
         return search[i]
         
       else: # if it isn't b:
         if b > list[search[i]]: # if the list search at position i is less than b, then the search is cut to being the remaining numbers to the right of i
           search = search[i+1:]
         elif b < list[search[i]]: # if the list search at position i is greater than b, then the search is cut to being the remaining numbers to the left of i
           search = search[:i+1]
   else: #if it gets through the entire list and didn't find anything, then you can have a -1
     return -1


'''Barry's Binary Search Function '''
def bsearch(l, s):
        found = False #Our indicator to exit the funciton and also tell us if the value was found
        startSearchParameter = 0
        endSearchParameter = len(l) - 1
        searchValue = s
        middleValue = None # MiddleValue has no value initially
        while (not found) and (startSearchParameter <= endSearchParameter): # We will iterate either until we find the value or we reach the end of the list indicated by the startSearchParameter equalling the endSearchParameter
                middleValue = ((startSearchParameter+endSearchParameter)/2)
                if searchValue == l[middleValue]:
                        found = True # Our indicator that we have "found" the searchValue
                else:
                        if searchValue < l[middleValue]:
                                endSearchParameter = middleValue - 1
                        else:
                                startSearchParameter = middleValue + 1
        if not found: # Test to see if the value was found, if not found will have a value of False
                 return -1
        else: # Will return middleValue if found is True
                 return middleValue


#Brittany Miller's binary search function

def bsearch(search_list, list_element):
    size=len(search_list)-1
    middle_point = size/2
    list_len=len(search_list)
    while size>0:
            if list_element == search_list[middle_point]:
                return middle_point
            elif list_element < search_list[middle_point]:
                middle_point = middle_point/2
                size-=1
            elif list_element < search_list[middle_point]:
                middle_point =(middle_point + list_len)/2
                size-=1
    return -1
    
#Boluwatife Aiki-Raji's Binary search
def bsearch (givenlist,element):
	start = 0
	end = len(givenlist)
	while start < end:
		midpoint = (start+end)/2
		if element < givenlist[midpoint]:
			end = midpoint 
		elif element > givenlist[midpoint]:
			start = midpoint + 1
		else:
			return midpoint
	return -1
#Bolu's Binary Search
