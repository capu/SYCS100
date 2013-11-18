#Maimuna Ahmed's code starts hur
def bsearch( alist , element):
	alist.sort()
	front = 0
	back = len(alist)-1
	found = True
	midpoint = (front + back)//2

	for i in range(len(alist)):

		if alist[midpoint] == element:
			return midpoint

		elif element > alist[midpoint]:
			front = midpoint + 1
			midpoint = (front + back)//2

		elif element < alist[midpoint]:
			back = midpoint - 1
			midpoint = (front + back)//2

	return -1
#Maimuna Ahmed's code ends hur
