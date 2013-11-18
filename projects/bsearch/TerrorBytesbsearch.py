#Hi prof pratt this is team TerrorBytes. The group members are:
#1.Roshan Thapaliya
#2. Prajjwal Dangal
#3. Nischal Baral
#4. Ram Hari Dahal
#5. Gyasi Jordan
#6. Tyriece McGlawn
#7. Jonathon Moody

"Roshan's final solution"

'doing binary search on list1'
'defining the function with parameters list1 and searchelement'
'sorting the list in ascending order'
'finding the length of the list'
'finding max boundary when searching the list'
'finding min boundary when seaching the list'
'initializing the loop. It ends when minimum boundary is less than or equal to maximum boundary'
'finding search position'
'inside the loop there are conditions to check if searchelement is found or which side of searchposition it is in. Here we also update the new searchposition'

def binary_search(list1,searchelement): 
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




#Tyriece McGlawn


def bSearch(theList, t):
    min = 0 
    max = len(theList) - 1
    while 1:
        if max < min:        #if the max value is less than the min then return -1 and assign m to a new value
            return -1
        m = (min + max) / 2
        if theList[m] < t:   #if the index m in theList is less than the parameter t, then assign min to a new value
            min = m + 1
        elif theList[m] > t: #if the index m in theList is greater than the parameter t, then assign max to a new value
            max = m - 1
        else:
            return m         #else the function will return the new value for m
theList = [1,2,3,4,5]
t = 3
print bSearch(theList, t)   #print the value
