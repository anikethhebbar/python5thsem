#setdefault()
spam={'name': 'Bob', 'age':5}
if 'color' not in spam:
    spam['color']='black'
print(spam)
#instead of above code we use this function
spam.setdefault('key','value')
print(spam)
