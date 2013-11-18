#bsearch group members:
#Elyon Olonaran
#Oreoluwa Onatemowo
#Selina Jones
#Maimuna Ahmed
#Nolan English
#Jahmaal Gayle




mylist=[0,6,98,1,4,88,33,91,43,90,78]
mylist.sort()
print mylist


def bsearch(mylist,x):
    size=len(mylist)
    low=0
    high=size
    if mylist==[]:
        return mylist
    if high==size:
        high =len(mylist)-1
    while low<=high:
        mid = (low+high)/2
        midval=mylist[mid]
        if midval<x:
            low=mid+1
        elif midval>x:
            high=mid
        else:
            return mid
    return -1
            
print bsearch([0,6,98,1,4,88,33,91,43,90,78],0)
