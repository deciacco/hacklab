from ctypes import *
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR, LPDWORD, DWORD, HANDLE, BOOL
from weakref import ref

#A <-- Ansi function
MessageBoxA = windll.user32.MessageBoxA
MessageBoxA.argtypes = (HWND, LPCSTR, LPCSTR, UINT)
MessageBoxA.restype = INT

lpText = LPCSTR(b"Hello World!")
lpCaption = LPCSTR(b"Python Calling Win API")
MB_OKCANCEL = 0x00000001

#print(MessageBoxA(None, lpText, lpCaption, MB_OKCANCEL))

GetUserNameA = windll.advapi32.GetUserNameA
GetUserNameA.argtypes = (LPSTR, LPDWORD)
GetUserNameA.restype = BOOL

buff_size = DWORD(7)
thebuff = create_string_buffer(buff_size.value)

GetUserNameA(thebuff, byref(buff_size)) 
print(thebuff.value)

error = GetLastError()

if error:
    print(WinError(error))

#https://docs.microsoft.com/en-us/windows/win32/api/windef/ns-windef-rect

class RECT(Structure):
    _fields_ = [("left", c_long),
                ("top", c_long),
                ("right", c_long),
                ("bottom", c_long)]

rect = RECT()

GetWindowRect = windll.user32.GetWindowRect
GetWindowRect.argtypes = (HANDLE, POINTER(RECT))
GetWindowRect.restype = BOOL

hwnd = windll.user32.GetForegroundWindow()
GetWindowRect(hwnd, byref(rect))

print(rect.left)
print(rect.top)
print(rect.right)
print(rect.bottom)