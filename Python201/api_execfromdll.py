from ctypes import *

print(windll.msvcrt.time(None))

windll.msvcrt.puts(b"print this!")

mut_str = create_string_buffer(10)
print(mut_str.raw)

mut_str.value = b"AAAAA"
print(mut_str.raw)

windll.msvcrt.memset(mut_str, c_char(b"X"), 5)
windll.msvcrt.puts(mut_str)
print(mut_str.raw)

lib = WinDLL("c:\\Users\\eugenio.cilento\\Dev\\hacklab\\Python201\\CallFromPy.dll")
lib.hello()

