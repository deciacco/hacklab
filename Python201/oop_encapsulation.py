# derived, child class
# base, parent class

# encapsulation good for accidental damage protection to attributes, not secure

# person class
class Person:
    'Person base class' #__doc__

    def __init__(self, name, age) -> None:
        self.__name = name # protected
        self.__age = age # protected

    #def __repr__(self) -> str:
    #    return "Hi, I'm {} and I'm {} years old.".format(self.__name, self.__age)

    def birthday(self):
        self.__age += 1

    def get_age(self) -> str:
        return str(self.__age)

    def set_age(self, age):
        self.__age = age
    
    # class attribute
    # if changed on class, all instanaces will reflect the change
    # if changed on the instance, only changed for that instance
    class_attr = True

# examples
# ****************************************************************

bob = Person("bob", 35)
print(bob.get_age())
print(bob.__dict__)
bob._Person__age = 45 # do not rely on encapsulation, can still be accessed
print(bob.get_age())