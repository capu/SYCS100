# hello teamates this is our file. add your code and comment your name

# Nolan English Code Follows

import random

List = []

x = 10

while x >= 0:
    random.seed()
    List.append(random.randint(1,10))
    x -= 1

x = 10

def sorting(a,d):
    c = 0
    a.sort()
    print a
    for i in a:
        if i == d:
            c += 1
    if c == 0:
        print "the value %s is not in the list try again" % (str(d))
    elif c > 1:
        print "their is more than one instance of what you are looking for: %s" %(str(d)) 
    elif c == 1:
        b = ((len(a) - 1) / 2)
        endpoint = len(a) -1
        startpoint = 0 
        while True:
            if d >= a[b]:
                startpoint = b
                while True:
                    if d > a[endpoint - ((endpoint-startpoint)/2)]:
                        startpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d < a[endpoint - ((endpoint-startpoint)/2)]:
                        endpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d == a[endpoint - ((endpoint-startpoint)/2)]:
                        print "the value %s is at %s\n" % (str(a[endpoint - ((endpoint-startpoint)/2)]) ,str(endpoint - ((endpoint-startpoint)/2))) 
                        break
                    if d == a[startpoint]:
                        print "the value %s is at %s\n" % (str(a[startpoint]),str(startpoint))
                        break
                    if d == a[endpoint]:
                        print "the value %s is at %s\n" %(str(a[endpoint]),str(endpoint))
                        break
                break
            break
        while True:
            if d <= a[b]:
                endpoint = b
                while True:
                    if d > a[endpoint - ((endpoint-startpoint)/2)]:
                        startpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d < a[endpoint - ((endpoint-startpoint)/2)]:
                        endpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d == a[endpoint - ((endpoint-startpoint)/2)]:
                        print "the value %s is at %s\n" % (str(a[endpoint - ((endpoint-startpoint)/2)]) ,str(endpoint - ((endpoint-startpoint)/2))) 
                        break
                    if d == a[startpoint]:
                        print "the value %s is at %s\n" % (str(a[startpoint]),str(startpoint))
                        break
                    if d == a[endpoint]:
                        print "the value %s is at %s\n" % (str(a[endpoint]),str(endpoint))
                        break
                break
            break
        if d == a[b]:
            print "wow its exactly in the middle"

while x > 0:
    sorting(List,x)
    x -=1

# Nolan English CODE ends
