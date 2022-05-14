# derived, child class
# base, parent class

# encapsulation good for accidental damage protection to attributes, not secure

# person class
from time import perf_counter


class Person:
    'Person base class' #__doc__

    def __init__(self, name, age) -> None:
        self.__name = name # protected
        self.__age = age # protected

    def __repr__(self) -> str:
        return "Hi, I'm {} and I'm {} years old.".format(self.__name, self.__age)

    def birthday(self):
        self.__age += 1

    def get_age(self) -> str:
        return str(self.__age)

    def set_age(self, age):
        self.__age = age
    
    @property # decorator
    def age(self):
        print("getting age")
        return self.__age

    @age.setter
    def age(self, age):
        print("setting age")
        self.__age = age

    @age.deleter
    def age(self):
        print("deleting age")
        del self.__age

    @classmethod # can only access class attributes, no instance
    def acc_class_attr(cls):
        return cls.class_attr

    @classmethod
    def bob_factory(cls):
        return cls("bob", 30)

    @staticmethod
    def static_print(): #subclass to change or overwrite a method
        print("I'm static")

    # class attribute
    # if changed on class, all instanaces will reflect the change
    # if changed on the instance, only changed for that instance
    class_attr = True

# examples
# ****************************************************************

bob = Person("bob", 30)

print(bob.age)
bob.age = 45
print(bob.age)
del bob.age

bob1 = bob.bob_factory()
bob2 = bob.bob_factory()

print(bob1)
print(bob2)