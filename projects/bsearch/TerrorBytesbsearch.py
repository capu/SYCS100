#Hi prof pratt this is team TerrorBytes. The group members are:
#1.Roshan Thapaliya
#2. Prajjwal Dangal
#3. Nischal Baral
#4. Ram Hari Dahal
#5. Gyasi Jordan
#6. Tyriece McGlawn
#7. Jonathon Moody

#Roshan Thapaliya

# 'doing binary search on list1'
# 'defining the function with parameters list1 and searchelement'
# 'sorting the list in ascending order'
# 'finding the length of the list'
# 'finding max boundary when searching the list'
# 'finding min boundary when seaching the list'
# 'initializing the loop. It ends when minimum boundary is less than or equal to maximum boundary'
# 'finding search position'
# 'inside the loop there are conditions to check if searchelement is found or which side of searchposition it is in. Here we also update the new searchposition'

def bsearch(list1,searchelement): 
    list1.sort()                        
    length=len(list1)                   
    max_val=length-1                    
    min_val=0                           
    while min_val<=max_val:             
        mid=(max_val+min_val)/2         

        if list1[mid]==searchelement:   
            return mid
        elif searchelement>list1[mid]:
            min_val=mid+1
        else:
            max_val=mid-1
    return -1


    
    
#Jonathon Moody
    
def bsearch(listm,element):
    Lo = 0
    Hi = len(listm)
    if Hi == 0:
        return -1
    while Lo < Hi:
        mid = (Lo+Hi)/2          #Have to find the midpoint first
        midvalue = listm[mid]
        if midvalue < element:       #if the value is less than the wanted value the function will search higher along the list
            Lo = mid + 1
        elif midvalue > element:     #if the value is greater than the wanted value the function will search lower along the list.
            Hi = mid
        elif midvalue == element:
            return mid               #Once mid equals the wanted value the function will return it.
        else:
            return -1



#Gyasi Jordan
def bsearch(listx,searchval):    
    listx.sort()
    cutvar = len(listx)/2
    midvalue = listx[cutvar]
    currentlist = listx
    while searchval != midvalue:
        if len(currentlist) == 1:
            if currentlist[0] == searchval:
                return midvalue
            else:
                return None
        if currentlist[cutvar] > searchval:
            currentlist = currentlist[0:cutvar]
        else:
            currentlist = currentlist[cutvar+1:len(currentlist)]
        cutvar = len(currentlist)/2
        midvalue = currentlist[cutvar]
    return midvalue     

print bsearch([1,2,3,4,5],4)



#PRAJJWAL DANGAL, email: prajjwal.dangal@bison.howard.edu

#defining a function that takes a list and an element whose index we want to find as its parameters.

def bsearch(thelist, element):

    #checking for empty list and list with only one element in it.

    if thelist == []:
        return -1
    if len(thelist) == 1 and element == thelist[0]:
        return 0

    thelist.sort()
    lengthlist = len(thelist)
    index = int(lengthlist/2)

    #remember is a variable that serves, along with index, the function of defining the maximum and minimum index between which the element should appear. 
    remember = lengthlist

    #for loop that runs over and over until we get the index of the element we are searching for in the list or until we return -1 if the element isn't there.

    for i in range (0, (lengthlist)):
        if element == thelist[index]:
            return index
        elif element < thelist[index]:
            #for this condition we only want to keep on cutting the index by half.
            remember = index
            index = index/2
        else:
            #for this condition we only want to assign index the average value of index and remember.
            index = (remember + index)/2
    if not index:
        return -1
# Nischal Baral

def bsearch(list, element):
 list.sort()
 length = len(list)
 N = length - 1
 size = 1
 if length == 0:  return -1
 if element==list[0]:  return 0
 if element==list[N-1]:  return N-1
 while N > 0 and N < length:
  if element == list[N]:
   return N
  elif element < list[N]:
   N = N- (length+1)//(2**size)
   size += 1
  elif element > list[N]:
   N= N + (length+1)//(2**size)
   size += 1
 return -1
 
 
 # Ram Hari Dahal
 
 def bsearch(myList, searchElement):  # declaration statement with a function name "bsearch" and parameters myList(which takes the list) and searchElement(which takes the element to search).
        myList.sort()               # sorting the list if not already sorted.
        myLength = len(myList)
        firstInd = 0
        lastInd = myLength - 1
        
        if myLength == 0 or myList == []: # checking for empty list 
                return -1

        while firstInd <= lastInd:
                half = (firstInd + lastInd)/ 2

                                
                if myList[half]== searchElement:
                        return half

                elif myList[half] > searchElement:
                        lastInd = half
                        half= (firstInd + lastInd)/2
                elif myList[half] < searchElement:
                        firstInd = half + 1
                        half= (firstInd + lastInd)/2
                        
        
        return -1
       
#Tyriece McGlawn

def bsearch(theList, t):
    min = 0
    max = len(theList) - 1
    while 1:
        if max < min:    #if the max value is less than the min then return -1 and assign m to a new value
            return -1
        m = (min + max) / 2
        if theList[m] < t:
            min = m + 1
        elif theList[m] > t: #if the index m in theList is greater than the parameter t, then assign max to a new value
            max = m - 1
        else:
            return m

theList = [1,2,3,4,5]
t = 4
bsearch(theList, t)

