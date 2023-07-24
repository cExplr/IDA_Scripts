import ida_dbg
import ida_idd
import ida_kernwin

# Process flag is in form of `DSTATE_*`
"""
DSTATE_SUSP            = -1 # process is suspended
DSTATE_NOTASK          =  0 # no process is currently debugged
DSTATE_RUN             =  1 # process is running
DSTATE_RUN_WAIT_ATTACH =  2 # deprecated
DSTATE_RUN_WAIT_END    =  3 # deprecated
"""
process_flag = ida_dbg.get_process_state()
if process_flag & DSTATE_SUSP and process_flag&DSTATE_RUN:


    print(f"Debugger is running ..")
    mod = ida_idd.modinfo_t()
    x = ida_dbg.get_first_module(mod)
    if x:
        print(f"-> 0x{mod.base:x} : {mod.name} , 0x{mod.size:x} bytes ")
        while ida_dbg.get_next_module(mod):
            print(f"-> 0x{mod.base:x} : {mod.name} , 0x{mod.size:x} bytes ")
            debug_names = ida_name.get_debug_names(mod.base, mod.base+mod.size)
            if debug_names:
                for ea, name in debug_names.items():
                    print(f"\t0x{ea:08x} - {name}")
                
        
    else:
        print("Done")
else:
    print(f"Debugger is not running!")


ea = ida_kernwin.get_screen_ea()
def get_debugname_from_ea(ea):
    print(f"Debug name from {ea:016x}")
    """
    FLAGS FOR HOW
    enum debug_name_how_t
    {
      DEBNAME_EXACT,        ///< find a name at exactly the specified address
      DEBNAME_LOWER,        ///< find a name with the address >= the specified address
      DEBNAME_UPPER,        ///< find a name with the address >  the specified address
      DEBNAME_NICE,         ///< find a name with the address <= the specified address
    };
    """
    dname = ida_name.get_debug_name(ea, ida_name.DEBNAME_EXACT)
    return dname
dname = get_debugname_from_ea(ea)
print(dname)