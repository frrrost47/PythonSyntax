# Set - неупорядоченная колекция с уникальными данными

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # {'orange', 'banana', 'pear', 'apple'}
'orange' in basket # true

a = set('abracadabra') # {'a', 'r', 'b', 'c', 'd'}
b = set('alacazam') #
a - b # {'r', 'd', 'b'}

a | b # {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}  # letters in a or b or both
a & b # {'a', 'c'}  # letters in both a and b
a ^ b # {'r', 'd', 'b', 'm', 'z', 'l'}  # letters in a or b but not both