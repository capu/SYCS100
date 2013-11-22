Bsearch

#Jacari Boboye
#Malik HornBuckle
#Isaiah Williams
#Justin Austin
#David Blackstone



def bsearch(List, number):
+	found = 0
+	lenList = len(List)-1
+	min = 0
+	max = lenList
+	x = 0
+	if max <= min:
+			return -1
+	else:	
+		while max >= min: 
+			x = (max + min)/2
+			if List[x] == number:
+				found = [x]
+				return x
+			elif List[x] < number:
+				min = x + 1
+			else: 
+				max = x - 1	
+		return found
+
+		


# Justin Austin


def binary_search(a, x, small=0, big=None):
    if big is None:
        big = len(a)
    while small < big:
        mid = (small+big)//2
        midval = a[mid]
        if midval < x:
            small = mid+1
        elif midval > x: 
            big = mid
        else:
            return mid
    return -1

#Jacari Boboye

def binarySearch(myItem,myList):
        found=False
        bottom=0
        top=len(myList)-1
        while bottom<=top and not found:
                middle = (bottom+top)//2
                if myList[middle]==myItem:
                        found =True
                elif myList[middle]< myItem:
                        bottom=middle +1
                else:
                        top=middle-1
        return found

# Kalen Collins

def bsearch(List, searchFor):

      high = len(List)-1 
      low = 0 
          
      while low <= high:
         
         if len(List) == 0: 
            return "Empty List"
         
         mid = (high + low)//2 
         
         if List[mid] < searchFor: 
            low = mid + 1
            
         elif List[mid] > searchFor: 
            high = mid - 1
            
         else:
            return mid 
         
