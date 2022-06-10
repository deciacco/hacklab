from ctypes import *
from ctypes import wintypes

#syscalls allow call without using dlls.
kernel32 = windll.kernel32
nt = windll.ntdll

SIZE_T = c_size_t
NTSTATUS = wintypes.DWORD

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40


