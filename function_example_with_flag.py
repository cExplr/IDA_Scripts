import ida_funcs
import idc
import ida_kernwin
 
def main():
    ea = idc.here()
    f = ida_funcs.get_func(ea)
    if not f:
        print(f"Not inside a function @ 0x{ea:x}")
        return False
    print(f"OK!")
    print("Start : ", hex(f.start_ea))
    print("  End : ", hex(f.end_ea))
    
    ## FLAGS 
    if f.flags & ida_funcs.FUNC_LIB:
        print("This is a library function")
    else:
        print("This is not a library function")
    
ida_kernwin.msg_clear()  
main()