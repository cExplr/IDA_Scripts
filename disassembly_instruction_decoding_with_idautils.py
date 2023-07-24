import idautils
import ida_kernwin

ea = ida_kernwin.get_screen_ea()

while True:
    inst = idautils.DecodeInstruction(ea)
    if not inst :
        break # Cannot decode
    if inst.itype: 
        # Can see this in IDC   decode_insn(here)
        # Can refer to both ua.hpp and allins.hpp (all instructions) for NN_* instructions
        # Can refer to intel.hpp as well for regnum or their respective architecture
        
        if inst.itype != idaapi.NN_push:
            continue # we only want the call function
            
        if instr.Op1.type != idaapi.o_imm:
            continue
            
        print(f"Pushed {instr[0].value:x}")