from ctypes import *
from ctypes.wintypes import POINT
import os
from re import X
from tkinter import Y
from turtle import st

curr_dir = os.path.dirname(os.path.realpath(__file__))

print(windll.msvcrt.time(None))

windll.msvcrt.puts(b"print this!")

mut_str = create_string_buffer(10)
print(mut_str.raw)

mut_str.value = b"AAAAA"
print(mut_str.raw)

windll.msvcrt.memset(mut_str, c_char(b"X"), 5)
windll.msvcrt.puts(mut_str)
print(mut_str.raw)

lib = WinDLL(os.path.join(curr_dir, "CallFromPy.dll"))
lib.hello()

lib.length.argtypes = (c_char_p,)
lib.length.restype = c_int

str1 = b"abc\x00123"
print(len(str1))
print(lib.length(c_char_p(str1)))

lib.add.argtypes = (c_int, c_int)
lib.add.restype = c_int
print(lib.add(2, 2))

lib.add_p.argtypes = (POINTER(c_int), POINTER(c_int), POINTER(c_int))

x = c_int(2)
y = c_int(4)
result = c_int(0)

lib.add_p(byref(x), byref(y), byref(result))

print(result.value)