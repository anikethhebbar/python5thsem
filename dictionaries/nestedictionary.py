allGuest = {'Alice': {'apples': 5,'pretzels':12},'Bob': {'ham': 3,'apples':2},'Carol': {'cups': 3,'apple pie':1}}
def total(guests, item):
    numBrought=0
    for k,v in guests.items():
        numBrought = numBrought+v.get(item,0)
    return numBrought
print("number of things bought")
print(' apples ' + str (total(allGuest, 'apples')))
print(' ham ' + str (total(allGuest, 'ham')))