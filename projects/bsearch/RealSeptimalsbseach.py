''' Group 5 Members:

Hannah M. Clark
Lena Alston
Cesa Salaam
Sarah Jones
Jabari Olatunji 
Contee Cameron 
Courtney Gaines
Attiyah Laneir
Alston Clark
'''





# Alston Clark

def bsearch(list,search):




  top = len(list)

  bottom = 0

  
 

  if (top < search) and (search < bottom):
    return -1 
  
  if (len(list) == 0):
    return -1 
    
   
  while ( bottom <= top):
  



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


def bsearch (List, element):
    bottom = 0
    top = len(List)-1
    if len(List)== 0:
        return -1
    elif len(List)!= 0:
        if element <= List[top] and element >= List[0]:
            
                while top >= bottom:
                    middle = (bottom+top)//2
                    if element == List[middle]:
                        return middle
                    elif element > List[middle]:
                        bottom = middle + 1
                    elif element < List[middle]:
                        top = middle - 1
        else:
            return -1
            
 


def bsearch_attiyah (searchList, element):
    first = 0 
    last = len(searchList) - 1    
    midPoint = (first + last) / 2       
    found = False    
    
    

    while found == False and first <= last:   
        
        if element > searchList[midPoint]:      
            first = midPoint + 1               
            midPoint = (first + last) /2        
            found = False                       

        elif element < searchList[midPoint]:    
            last = midPoint - 1                 
            midPoint = (first + last) / 2       
            found = False                       

        elif element == searchList[midPoint]:   
            found = True                        

    if found == False:                         
        return -1

    
    return midPoint                             




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



#Lena's bsearch 

def bsearch(list, element):             
    if len(list) != 0:                    
        first = 0                   
        last = len(list)-1              
        found = False                      
        while not found:                 
            midpoint = (first + last)/2        
            if (first==last) and (element != list[first]):             
                return -1                                 
            elif element < list[midpoint]:             
                last = midpoint - 1                  
            elif element > list[midpoint]:              
                first = midpoint + 1                 
            else:                                      
                found = True                       
                return midpoint     
    else:                           
   
        return -1


#Sarah Jones
def bsearch( lista, element):
    start = 0
    end = len(lista) - 1
    while (end >= start):
          mid = (start + end) / 2
          if (lista[mid] < element):
            start = mid + 1
          elif lista[mid] > element:
            end = mid - 1
          else:
            return mid
            
        
    return -1
    
#Contee Cameron's Search 

def  bsearch(ist, item):
  
  if len(ist) == 0:
      
      return -1

    low = 0

    up = len(ist)-1
    

    while low <= up:
            
        mid= (low + up) / 2
        
        
        if ist[mid] < item:

            low = mid +1
            

        elif ist[mid] > item:

            up = mid - 1
            

        elif ist[mid] == item: 
    
            return mid

        else:
            return -1

# Jabari's Code
def bsearch(list,item):
    
      top =  len(list)-1
      
      bottom = 0
      
      found = False
      
      while found == False:
          
          search = (top+bottom)/2
          
          if item > list[search]:
              
             bottom = search + 1
             
        
          elif item < list[search]:
              
              top = search -1
          if item not in list:
              return -1  
            
              
          elif item == list[search]:
    
              return search
