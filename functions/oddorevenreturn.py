# Check whether the given statement  is even or odd with return
def evenodd(num1):
    
    if num1%2==0:
        return 0
    return 1
num1=int(input("Enter number: "))
num=evenodd(num1)
if num == 0:
    print("EVEN")
else:
    print("odd")
