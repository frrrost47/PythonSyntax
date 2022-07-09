tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
del tel['sape']

list(tel) # list of key value

print(sorted(tel)) # list sorted keys
print(tel)

'guido' in tel

{x: x**2 for x in (2, 4, 6)} # {2: 4, 4: 16, 6: 36}

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v)