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