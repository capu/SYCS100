''' Team r3-Bo0t 
	Barry Harris
	Errol Grannum
	Boluwatife Aiki-Raji
	Hallie Lomax
	Brittany Miller
	Eric Walker '''




# Chris Quist's binary search
def bsearch(wlist, item):
    beginning=0
    end = len(wlist)
    while beginning!=end:
        middle = (beginning + end)/2
        if item == wlist[ middle]:
            return middle
        elif item < wlist[middle]:
            end = middle
        else:
            if beginning == middle:
                return -1
            else:
                beginning = middle
    return -1
