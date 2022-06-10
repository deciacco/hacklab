# https://docs.python.org/3/library/ctypes.html#ctypes.c_long

from ctypes import *

b0 = c_bool(0)
b1 = c_bool(1)

print(b0)
print(b1)

print(b0)
print(type(b0))
print(b0.value)

print(b1)
print(type(b1))
print(b1.value)

#--------------------------------------------------
print ("-"*50)
#--------------------------------------------------

#c_unit alias for c_ulong
print("Unsigned Long Int i0 = c_uint(-1) | 0 to " + str(c_uint(-1)))

#--------------------------------------------------
print ("-"*50)
#--------------------------------------------------

c0 = c_char_p(b"test")
print("c0 = c_char_p(b\"test\") | c0.value = " + str(c0.value))
print("print(c0) = " + str(c0))

c0 = c_char_p(b"test2")
print(c0)
print(c0.value)

#--------------------------------------------------
print ("-"*50)
#--------------------------------------------------

p0 = create_string_buffer(16) #creates a pointer
print(p0)
print(p0.raw)
print(p0.value)

p0.value = b"a"
print(p0)
print(p0.raw)
print(p0.value)

#--------------------------------------------------
print ("-"*50)
#--------------------------------------------------

i = c_int(42) 

print(i) 
print(pointer(i))
print(pointer(i).contents)
print(hex(addressof(i)))

pt = byref(p0)
print(cast(pt, c_char_p).value)

print(cast(pt, POINTER(c_int)).contents)
print(ord('a'))

#--------------------------------------------------
print ("-"*50)
#--------------------------------------------------

class PERSON(Structure):
    _fields_ = [("name", c_char_p),
                ("age", c_int)]

person_array_t = PERSON * 3
person_array = person_array_t()

person_array[0] = PERSON(b"bob", 30)
person_array[1] = PERSON(b"alice", 32)
person_array[2] = PERSON(b"joe", 29)

for person in person_array:
    print(person)
    print(person.name)
    print(person.age)