import ida_idd

"""
 |  proto(name_or_ea, proto_or_tinfo, flags=None)
 |      Allows you to instantiate an appcall (callable object) with the desired prototype
 |      @param name_or_ea: The name of the function (will be resolved with LocByName())
 |      @param proto_or_tinfo: function prototype as a string or type of the function as tinfo_t object
 |      @return:     - On failure it raises an exception if the prototype could not be parsed
 |            or the address is not resolvable
 |          - Re
"""
 
# Library location is resolved via LocByName under the hood
loadlib = ida_idd.Appcall.proto("kernel32_LoadLibraryA", "HMODULE loadlib(const char *);")
print("Loading library user32.dll")
loadlib("user32.dll") # Call the function

print("Calling messagebox")
MB_OK = 0
MB_YESNO = 4
NULL = 0
msgbox = ida_idd.Appcall.proto("user32_MessageBoxA", "int msgbox(HWND,LPCSTR,LPCSTR,UINT);")
msgbox(NULL,"Here is the main message","Message",MB_OK)