def colatz(number):
       if (number%2==0) :
            return number=number//2)
       else:
            print(number=(3*number)+1)
n = int(input("Enter a Number"))
i=colatz(n)
if i !=1:
    colatz(i)