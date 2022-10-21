def spam():
    eggs = 'local spam'
    print(eggs)
def bacon():
    eggs='bacon local'
    print(eggs)
    spam()
    print(eggs)
eggs='global'
bacon()
print(eggs)


