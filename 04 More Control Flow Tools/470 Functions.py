def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# fib(100) # 0 1 1 2 3 5 8 13 21 34 55 89
# f = fib(10) # 0 1 1 2 3 5 8


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

#print(fib2(20))

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

i = 5

def f(arg=i):
    print(arg)

i = 6
# f() # 5

# непривычно работает память:

def f1(a, L=[]):
    L.append(a)
    return L

def f2(a, L=[]):
    L.append(a)
    return L

print(f(1), f(2), f(3), f2(4), f2(5), f2(6))


list = [[[1], 2], [3]]

array2 = list[0]

array2[0][0] = 99
print(list)

# * = list, **=array
def cheeseshop(kind, *arguments, **keywords):
    print("kind = ", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for key, value in keywords.copy().items():
        print(key, ":", value)

cheeseshop("Test", "1", "2", aaa="3", ooo="4", eee="5")