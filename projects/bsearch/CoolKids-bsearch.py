Group Members


Dontrell Knighten
Glenisha Smith
Travon Speller
Jabari Olatunji
Oluwatoorese Lasebikan
Christian Quist


Solutions:


def bSearch(searchList, target):
   low = 0
   high = len(searchList)
   while low <= high:
      if len(searchList)==0:
         return "EMPTY LIST"
      testpos = low + (high-low)/2
      ITEM = searchList[testpos]
      if ITEM == target:
         return testpos            
      elif ITEM < target: 
         low = testpos+1
      else:
         high = testpos-1
