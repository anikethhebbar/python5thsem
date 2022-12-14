#write a python program to count number of occurances of each letter in a string?
message="It was a bright cold day in April, the clock were striking thirteen"
count={}
for characters in message:
    count.setdefault(characters, 0)
    count[characters]=count[characters]+1
print(count)