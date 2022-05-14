print(1+1)
print("1"+"1")

# derived, child class
# base, parent class

# person class
class Person:
    'Person base class' #__doc__

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # overloaded method
    def __repr__(self) -> str:
        return "Hi, I'm {} and I'm {} years old.".format(self.name, self.age)

    # overloaded "+"
    def __add__(self, other): # other is expected to be the same type of object
        return self.age + other.age

    def __lt__(self, other):
        return self.age < other.age

    def birthday(self):
        self.age += 1
    
    # class attribute
    # if changed on class, all instanaces will reflect the change
    # if changed on the instance, only changed for that instance
    class_attr = True


# examples
# ******************************************************************

bob = Person("bob", 30)
alice = Person("alice", 22)

print(bob + alice)
print(bob < alice)