from cgitb import handler
from ctypes import *
from ctypes import wintypes
import os
import re

CURR_DIR = os.path.dirname(__file__)

dll = os.path.join(CURR_DIR, "Dll1.dll").encode()

kernel32 = windll.kernel32
SIZE_T = c_size_t

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_READWRITE = 0x04
EXECUTE_IMMEDIATELY = 0x0
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0x00000FFF)

class _SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        ('nLength', wintypes.DWORD),
        ('lpSecurityDescriptor', wintypes.LPVOID),
        ('bInheritHandle', wintypes.BOOL)       
    ]

SECURITY_ATTRIBUTES     = _SECURITY_ATTRIBUTES
LPSECURITY_ATTRIBUTES   = POINTER(SECURITY_ATTRIBUTES)
LPTHREAD_START_ROUTINE  = wintypes.LPVOID

OpenProcess             = kernel32.OpenProcess
OpenProcess.restype     = wintypes.HANDLE
OpenProcess.argtypes    = [
        wintypes.DWORD,
        wintypes.BOOL,
        wintypes.DWORD
    ]

VirtualAllocEx          = kernel32.VirtualAllocEx
VirtualAllocEx.restype  = wintypes.LPVOID
VirtualAllocEx.argtypes = [
        wintypes.HANDLE,
        wintypes.LPVOID,
        SIZE_T,
        wintypes.DWORD,
        wintypes.DWORD
    ]

WriteProcessMemory          = kernel32.WriteProcessMemory
WriteProcessMemory.restype  = wintypes.BOOL
WriteProcessMemory.argtypes = [
        wintypes.HANDLE,
        wintypes.LPVOID,
        wintypes.LPCVOID,
        SIZE_T,
        POINTER(SIZE_T)
    ]

GetModuleHandle             = kernel32.GetModuleHandleA
GetModuleHandle.restype     = wintypes.HMODULE
GetModuleHandle.argtypes    = [
        wintypes.LPCSTR
    ]

GetProcAddress              = kernel32.GetProcAddress
GetProcAddress.restype      = wintypes.HMODULE
GetProcAddress.argtypes     = [
        wintypes.HMODULE,
        wintypes.LPCSTR
]

CreateRemoteThread          = kernel32.CreateRemoteThread
CreateRemoteThread.restype  = wintypes.HANDLE
CreateRemoteThread.argtypes = [
        wintypes.HANDLE,
        LPSECURITY_ATTRIBUTES,
        SIZE_T,
        LPTHREAD_START_ROUTINE,
        wintypes.LPVOID,
        wintypes.DWORD,
        wintypes.LPDWORD
    ]


#-----------------------------------------------------------
pid = 16296

handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)

if not handle:
    raise WinError()

print("Handle obtained => {0:X}".format(handle))

remote_memory = VirtualAllocEx(handle, False, len(dll) + 1, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE)

if not remote_memory:
    raise WinError()

print("Memory allocated => ", hex(remote_memory))

write = WriteProcessMemory(handle, remote_memory, dll, len(dll) + 1, None)

if not write:
    raise WinError()

print("Bytes written => {}".format(dll))

load_lib = GetProcAddress(GetModuleHandle(b"kernel32.dll"), b"LoadLibraryA")

print("LoadLibrary address => ", hex(load_lib))

if not load_lib:
    raise WinError()

rthread = CreateRemoteThread(handle, None, 0, load_lib, remote_memory, EXECUTE_IMMEDIATELY, None)