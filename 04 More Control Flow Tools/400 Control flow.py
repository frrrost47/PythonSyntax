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

# 0..<3
for i in range(3):
    print(i) # 012

# 5..<10
list(range(5, 10)) # [5, 6, 7, 8, 9]

# шаг 3
list(range(0, 10, 3)) #[0, 3, 6, 9]
# шаг -30
list(range(-10, -100, -30)) # [-10, -40, -70]


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
            # continue
    else:
        # if break
        print(n, 'is a prime number')

# pass - Заявление passничего не делает.
# Его можно использовать, когда оператор требуется синтаксически
# но программа не требует никаких действий. Например:
class MyEmptyClass:
    pass # Remember to implement this!

def initlog(*args):
    pass   # Remember to implement this!


# match
# Оператор matchпринимает выражение и сравнивает его значение с последовательными шаблонами,
# заданными в виде одного или нескольких блоков case. Внешне это похоже на оператор switch в Swift

def http_error(status):
    match status:
        case 400 | 401:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

def where_is2(point):
    match points:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")

def where_is3(point):
    match point:
        case Point(x, y) if x == y:
            print(f"Y=X at {x}")
        case Point(x, y):
            print(f"Not on the diagonal")