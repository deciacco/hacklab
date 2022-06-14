from ctypes import *
from ctypes import wintypes

#https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualprotect
#https://j00ru.vexillium.org/syscalls/nt/64/
#syscalls allow api calls without using dlls.
#0x0018 = NtAllocateVirtualMemory
kernel32 = windll.kernel32
nt = windll.ntdll

SIZE_T = c_size_t
NTSTATUS = wintypes.DWORD

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40

#windows will also execute syscall like this when win32api used
"""
mov r10, rcx
move eax, 18h   move the syscall by number into eax
syscall         call the syscall
ret

Steps
    write asm as shell code
    shell in memory
    update memory enable execution
    call it
"""

def verify(x):
    if not x:
            raise WinError()
"""
#use x64dbg to convert asm to shell code
#x64dbg-->attach-->notepad-->Binary, Fill w NOPs-->RC, Assemble-->"mov eax, 5; ret"

#put the shell code in memory
buf = create_string_buffer(b"\xb8\x07\x00\x00\x00\xc3")
buf_addr = addressof(buf)
print(hex(buf_addr))

#need to mark that page as executable or can't run the code
VirtualProtect = windll.kernel32.VirtualProtect
VirtualProtect.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.LPDWORD)
VirtualProtect.restype = wintypes.INT
old_protection = wintypes.DWORD(0)

protect = VirtualProtect(buf_addr, len(buf), PAGE_EXECUTE_READWRITE, byref(old_protection))
verify(protect)

#call our asm code
asm_type = CFUNCTYPE(c_int)#function definition
asm_function = asm_type(buf_addr)
r = asm_function()
print(hex(r))
"""
#***************************************************************
#----------------------------------------------￬￬￬ - NtAllocateVirtualMemory 
buf2 = create_string_buffer(b"\x4c\x8b\xd1\xb8\x18\x00\x00\x00\x0f\x05\xc3")
buf2_addr = addressof(buf2)
print(hex(buf2_addr))

#need to mark that page as executable or can't run the code
VirtualProtect = windll.kernel32.VirtualProtect
VirtualProtect.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.LPDWORD)
VirtualProtect.restype = wintypes.INT
old_protection = wintypes.DWORD(0)

protect = VirtualProtect(buf2_addr, len(buf2), PAGE_EXECUTE_READWRITE, byref(old_protection))
verify(protect)

hndl = 0xffffffffffffffff
base_adrs = wintypes.LPVOID(0x0)
zero_bits = wintypes.ULONG(0)
mem_size = wintypes.ULONG(1024 * 22)

#function definition
syscall_type = CFUNCTYPE(NTSTATUS, wintypes.HANDLE, POINTER(wintypes.LPVOID), wintypes.ULONG, POINTER(wintypes.ULONG), wintypes.ULONG, wintypes.ULONG)

syscall_function = syscall_type(buf2_addr)

ptr2 = syscall_function(hndl, byref(base_adrs), zero_bits, byref(mem_size), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

if ptr2 != 0:
        print(ptr2)

print("NtAllocateVirtualMemory: ", hex(base_adrs.value))

input()