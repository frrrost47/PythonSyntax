# тут tricks будет глобальным для всех экземпляров
class Dog:
    tricks = [] # будет изменяться глобально для всех собак сразу
    kind: str = 'canine'         # class variable shared by all instances

    def add_trick(self, trick):
        self.tricks.append(trick)

    # init сам создаст переменную name
    def __init__(self, name: str):
        self.name = name    # instance variable unique to each instance

# firstDog = Dog("First")
# secondDog = Dog("Second")
#
# firstDog.add_trick("111")
# secondDog.add_trick("222")
#
# print(firstDog.tricks)

# В этом классе tricks будут индивидуальны для каждого экземпляра так как
# инициализатор теперь будет делать из него отдельный объект в памяти
class SnupDog:

    tricks = []

    def __init__(self, name):
        self.name = name
        self.tricks = [1]    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

firstDog = SnupDog("First")
secondDog = SnupDog("Second")

firstDog.add_trick("111")
secondDog.add_trick("222")

print(firstDog.tricks)
print(secondDog.tricks)
