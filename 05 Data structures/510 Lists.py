fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.index('banana')
fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.reverse()
fruits.append('grape')
fruits.sort()
fruits.pop() # remove last


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

transposed = []

for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

del transposed[0:2]
print(transposed)