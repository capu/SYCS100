'''Hi prof pratt this is team TerrorBytes. The group members are:
1.Roshan Thapaliya
2. Prajjwal Dangal
3. Nischal Baral
4. Ram Hari Dahal
5. Gyasi Jordan
6. Tyriece McGlawn
7. Jonathon Moody '''

def binary_search(list1,searchitem):
    list1.sort()
    length=len(list1)
    mid=length/2
    
    
    for i in range (length):
        if mid>len(list1) or mid<0:
            return False
        if mid==0:
            if list1[0]==searchitem:
                return True
            else:
                return False
            
        
        if list1[mid]==searchitem:
            return True
        elif list1[mid]<searchitem:
            mid=mid+(mid/2)
        else:
            mid=mid-(mid/2)

    
    
    return False
    

        



print binary_search([1,2,3],3)


    
    
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
                return mid   #Once mid equals the wanted value the function will return it.
        else:
            return -1


a = [1,3,2,4,6,7,8,9]

print bsearch(a,4)

