aimport ida_idd

"""
According to IDA's help, dbg_appcallcalls application function after supplying the address to call, type and arguments. It returns the result of the function call.
It is easier to use IDC to use this because of the tight integration between interpreter and IDA kernel. It is still possible to so in idapython. We are interested in ida_idd.Appcall function. Also, to do this, we need the debugger to be running in the first place.
"""
eax_value = idaapi.get_reg_val("eax")
print(ida_idd.Appcall._B(eax_value))
