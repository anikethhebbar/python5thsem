d={'color': 'red', 'age':7}
print(d.keys())
#keys() for printing keys
print(d.values())
#values() for printing values
for k in d.keys():
    print(k)
for k,v in d.items():
    print("key "+ k+"value " + str(v))