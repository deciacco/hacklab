from ctypes import *
from ctypes import wintypes

kernel32 = windll.kernel32
nt = windll.ntdll

SIZE_T = c_size_t
NTSTATUS = wintypes.DWORD

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40

VirtualAlloc = kernel32.VirtualAlloc
VirtualAlloc.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD)
VirtualAlloc.restype = wintypes.LPVOID

NtAllocateVirtualMemory = nt.NtAllocateVirtualMemory
NtAllocateVirtualMemory.argtypes = (wintypes.HANDLE, POINTER(wintypes.LPVOID), wintypes.ULONG, POINTER(wintypes.ULONG), wintypes.ULONG, wintypes.ULONG)
NtAllocateVirtualMemory.restype = NTSTATUS


#--------------------------------------------------
ptr = VirtualAlloc(None, 1024 * 4, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

err = GetLastError()

if err:
        print(WinError(err))

print("VirtualAlloc: ", hex(ptr))

#--------------------------------------------------

hndl = 0xffffffffffffffff
base_adrs = wintypes.LPVOID(0x0)
zero_bits = wintypes.ULONG(0)
mem_size = wintypes.ULONG(1024 * 12)

ptr2 = NtAllocateVirtualMemory(hndl, byref(base_adrs), zero_bits, byref(mem_size), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

err = GetLastError()

if ptr2 != 0:
        print(ptr2)

print("NtAllocateVirtualMemory: ", hex(base_adrs.value))

#--------------------------------------------------
input()