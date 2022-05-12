from unicodedata import name

class Person:
    'Person base class' #__doc__

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return "Hi, I'm {0} and I'm {1} years old.".format(self.name, self.age)

    def birthday(self):
        self.age += 1
    
    # class attribute
    # if changed on class, all instanaces will reflect the change
    # if changed on the instance, only changed for that instance
    class_attr = True

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)

bob = Person("bob", 30)

print(bob)

print ("-"*50)

print("Has Attr: %s" % str(hasattr(bob, "attname")))
setattr(bob, "attname", 100)
print(getattr(bob, "attname"))
delattr(bob, "attname")

print ("-"*50)

del bob.name # removes attribute
del Person # remove definition of class, no new instances, existing instances are not destroyed