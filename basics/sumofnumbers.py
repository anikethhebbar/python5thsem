n=int(input("Enter the number: "))
s=0

while(n!=0):
    rem = n%10
    s=s+rem
    n=int(n)/10
print(int(s))