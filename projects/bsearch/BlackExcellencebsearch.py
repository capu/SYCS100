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
