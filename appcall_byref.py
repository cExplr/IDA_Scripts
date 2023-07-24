import ida_idd

a = ida_idd.Appcall

getcurdir = a.proto("kernel32_GetCurrentDirectoryA","DWORD __stdcall GetCurrentDirectoryA(DWORD nBufferLength, LPSTR lpBuffer);")

# BUFFER IS PASSED IN BY REFERENCE
currdir_buff = a.byref("\x00"*260)
getcurdir(260,currdir_buff)	
print(f"Current Directory at {currdir_buff.cstr()}")

## Another way is to create buffer with a.buffer



getwindir = a.proto("kernel32_GetWindowsDirectoryA",
"UINT __stdcall GetWindowsDirectoryA(LPSTR lpBuffer, UINT uSize);")

# Create buffer with the buffer function 
windir_buffer = a.buffer(size=260)
n = getwindir(windir_buffer, windir_buffer.size)
if n== 0:
    print("Could not get Windows directory")
else:
    print(windir_buffer.value[:n])