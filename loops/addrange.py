def sumofrange(num, num1): 
    sum=0
    for i in range(num, num1+1):
        sum= sum+i
    return sum

num= int(input("Number daalo bhai pehla wala? : "))
num1= int(input("Number daalo bhai kitne baar number tak karna? : "))
print(sumofrange(num, num1))