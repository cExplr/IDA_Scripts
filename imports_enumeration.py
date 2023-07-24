import ida_nalt

"""
Enumeration with callbacks

def enum_import_names(mod_index, callback):
 
    Enumerate imports from a specific module.
    Please refer to ex_imports.py example.

    @param mod_index: The module index
    @param callback: A callable object that will be invoked with an ea, name (could be None) and ordinal.
    @return: 1-finished ok, -1 on error, otherwise callback return value (<=0)
    
    
def get_import_module_name(path, fname, callback):
 
    Returns the name of an imported module given its index
    @return: None or the module name
    
    

//-------------------------------------------------------------------------

py_import_enum_cb

// callback for enumerating imports
// ea:   import address
// name: import name (nullptr if imported by ordinal)
// ord:  import ordinal (0 for imports by name)
// param: user parameter passed to enum_import_names()
// return: 1-ok, 0-stop enumeration
"""

def print_name(ea,name,o):  # o refers to ordinal
    print(f"\t0x{ea:x}/#{o}\t{name}")
    return 1

qty = ida_nalt.get_import_module_qty()
print(f"We have {qty} import modules")

for idx in range(qty):
    print(f"module name : {ida_nalt.get_import_module_name(idx)}")
    ida_nalt.enum_import_names(idx,print_name)
    
    
