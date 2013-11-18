# Alston Clark

def bsearch(list,search):




  top = len(list)

  bottom = 0

  
 

  if (top >= search >= bottom):
    return -1 

   
  while ( bottom != top):
    # when bottom == top then you have found the index

    mid = (top + bottom) / 2

    if (search < list[mid]):
      top = mid - 1


    elif ( search > list[mid]):
      bottom = mid + 1


    else:
      return mid


# Hannah's Bsearch

def search(item,numbers):
        searchend=len(numbers)                                          # end of search
        search=0                                                                        # start of search
        found=False
        while(found==False):
                scope=(search+searchend)/2                              # scope to hold span of search
                if(item<numbers[scope]):
                        searchend=scope-1
                elif(item>numbers[scope]):
                        search=scope+1
                else:                                                                   # if its is not greater or less than it is equal to
                        found=True
                        return scope                                            # return correct index






#Courtney Gaines

def bsearch(listt,e):
    start = 0
    end = len(listt)-1
    mid = (start + end) /2
    while (e != mid and start<end):
        if e < listt[mid]:  
            end = mid-1
            mid = (start + end)/2
        elif e> listt[mid]: 
            start = mid + 1
            mid = (start + end) /2
        else:
            return mid 
    return -1  





