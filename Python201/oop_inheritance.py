# derived, child class
# base, parent class

# person class
class Person:
    'Person base class' #__doc__

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return "Hi, I'm {} and I'm {} years old.".format(self.name, self.age)

    def birthday(self):
        self.age += 1
    
    # class attribute
    # if changed on class, all instanaces will reflect the change
    # if changed on the instance, only changed for that instance
    class_attr = True

# hacker class, derived from person
class Hacker(Person):
    'Hacker derived class'
    
    def __init__(self, name, age, pwns) -> None:
        super().__init__(name, age)
        self.pwns = pwns

    def __repr__(self) -> str:
        return "Hi, I'm Hacker {} and I have {} pwns!".format(self.name, self.pwns)

# examples
# ****************************************************************
bob = Person("bob", 30)
alice = Hacker("alice", 22, 89)

print(bob)
print(alice)


print(issubclass(Hacker, Person))
print(issubclass(Person, Hacker))
print(isinstance(bob, Hacker))
print(isinstance(bob, Person))