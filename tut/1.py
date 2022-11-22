# python code for to add an element to the list at a specified index
mylist = []
i=5
while(i):
    a = int(input("ENTER INDEX OF THE ELEMENT YOU WANNA ADD: "))
    b = str(input("Enter the element you wanna insert: "))
    mylist.insert(a, b)
    print(mylist)
    i-=1
