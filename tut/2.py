# Python program to remove all occurances of a given element from the list.
spam = [1, 2, 3, 4]

n = int(input("Enter numnber you wannna delete"))
print(len(spam))
for i in range(0,(len(spam)+1)):
    print(spam[i])
    if (spam[i]==n):
        spam.remove(n)
print(spam)