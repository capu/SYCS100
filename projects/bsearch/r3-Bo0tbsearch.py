''' Team r3-Bo0t 
	Barry Harris
	Errol Grannum
	Boluwatife Aiki-Raji
	Hallie Lomax
	Brittany Miller
	Eric Walker 
	Chris Quist'''

##Eric Walker
listA= [-1, 2, 3, 4, 555, 1, 2, 3, 4]  ##creates an initial list
listB= [2, 7, 4, 1, 8, 3]  ##creates a second list to add to the initial list
b = 0   ##sets a value to help stop the while loop
y = 1  ##defines the variable in the function
def sortingsort(y):  ##defines a function
    then = len(listB) > 0  ##assigns 'then' to be the boolean of len(listB) > 0
    x = then ##assigns 'then' to 'x'
    while x == True: ##while len (listB) > 0...
        c = listB[0 + b] ##assigns c to be the index of listB at 0 + b
        if c > listA[0]: ##checks if c > listA at index 0
            listA.append(c) ##adds c to listA
            listB.remove(c) ##removes x from listB
        elif c < listA[0]: ##checks if c < List A at index 0
            listA.append(c) ##adds c to list A
            listB.remove(c) ##removes c from list b
        else:
            listA.append (c) ##adds c to list A if c == list a index 0
            listB.remove(c) ## removes c from list be if c == list a index 0
        if len(listB) == 0: ## stops the function once list b is empty
            print 'Done combining. Sorting final list...' ##tells you what it is doing next
            finalList = sorted(listA) ##sorts list A and assigns it to finalList
            print finalList ##prints finalList
            return ##exits the function
sortingsort(y) ##runs the function

def bitSearch(y, s): ##begin bitsearch of y and the search variable
    sortingsort(y) ##calls the function sortingsort(y)
    print "Please wait while we attempt to find your query..." ##explains what it is doing
    extant = False ##assigns extant to be false
    startingPara = 0 ##assigns the starting parameter to equal 0
    endingPara = len(y) - 1 ##assigns the ending parameter to be the length of the list minus 1 since the length of a list is going to be 1 more than the final index
    search = s ##assigns search to be s
    while ((endingPara > startingPara + 1) and (extant == False)): ##says that while the ending is > starting + 1 (to even out the minus 1 of ending) and extant does not equal true
        midpoint = ((startingPara + endingPara) // 2) ##assigns the midpoint to be half of the sum of the starting and ending paras
        if search < y[midpoint]: ##sees if search is < y at the index of the midpoint
            endingPara = midpoint - 1 ##if so, the ending para now is the midpoint minus 1 to shift the function
        elif search > y[midpoint]: ##sees if search is  > y at index of the midpoint
            startingPara = midpoint + 1 ## if so, the starting para now is the midpoint + 1 to shift the function
        elif search == y[midpoint]: ## checks to see if the search is y index midpoint
            extant = True ##if so, extant = True, stopping the while loop
            print 'We found it, we found it, we found it, Yay!' #this is printed to assure the user that the search was found
        else:
            print 'Computer malfunction. Self destruct sequence activated. Please check search request...' ##tells the user that the search value was not found
bitSearch(listA, 8) ##runs the bit search when y = listA and s = 8



