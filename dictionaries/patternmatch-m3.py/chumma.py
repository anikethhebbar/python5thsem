import re 
phone=re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
mo=phone.search('My number is 123-434-2222')
mo.group
print(mo.group())