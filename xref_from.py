import ida_xref
import ida_kernwin

# Clear console
idaapi.msg_clear()

ea = ida_kernwin.get_screen_ea()
print(f"Address 0x{ea:08x} leads to:")
xref = ida_xref.xrefblk_t()
for xb in xref.refs_from(ea,ida_xref.XREF_ALL):
    print(f"\t--> 0x{xb.to:08x}")