
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

