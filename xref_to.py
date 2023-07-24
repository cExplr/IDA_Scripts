import ida_xref
import ida_kernwin
import ida_name
import idaapi

# Clear console
idaapi.msg_clear()
function_name = "_ZN6PlayerD2Ev"

#ea = ida_kernwin.get_screen_ea()
ea = ida_name.get_name_ea(idaapi.BADADDR, function_name)

print(f"Address 0x{ea:08x} is accessed by :")
xref = ida_xref.xrefblk_t()
for xb in xref.refs_to(ea,ida_xref.XREF_ALL):
    if not xb.iscode:continue
    print(f"\t--> 0x{xb.frm:08x}")