import idautils
import ida_kernwin

ea = ida_kernwin.get_screen_ea()

"""
        # Can see this in IDC   decode_insn(here)
        # Can refer to both ua.hpp and allins.hpp (all instructions) for NN_* instructions
        # Can refer to intel.hpp as well for regnum or their respective architecture
"""

inst = idautils.DecodeInstruction(ea)
if inst :
    if inst.Op1 == idautils.procregs.rax :
        print("Found!")
    else:
        print("Nope...")
