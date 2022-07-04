# if
x = 1
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# for
words = ['111', '222', '333']
for w in words:
    print(w, len(w))

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for key, value in users.copy().items():
    print(key, value)
    if value == 'inactive':
        del users[key]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status




