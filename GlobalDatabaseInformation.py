import ida_ida

# THIS DOES NOT SHOW THE EXHAUSTIVE LIST OF GETTERS OR SETTERS. REFER BACK TO SDK PLEASE


#Example of inf usage (Going to be obsolete soon)
print(idaapi.inf_get_procname())

# Use this instead
# Use getters and setters to global variables
# Look at lflags under idainfo structure

print("Assmebler  type index : ", ida_ida.inf_get_asmtype())
print("File is ELF : ", idaapi.inf_get_filetype() == idaapi.f_ELF)

  # Return the index of the selection
# Check if "Create Function Fails" analysis flag is set
if ida_ida.inf_get_af() & ida_ida.AF_FTAIL:
  print("Analysis flag Create Function Tails is set")
else:
  print("NOOOO... Analysis flag Create Function Tails is not set")
  
# Get Database Base Address ( change Segment offset when loading)
print(f"Base Address : {idaapi.inf_get_baseaddr():x}")
print(f"StartIP={idaapi.inf_get_start_ip():x}")
print(f"StartEA={idaapi.inf_get_start_ea():x}")
print(f"mainea={idaapi.inf_get_main():x}")

# Can use the following to get the program boundary for things like searching. min_eaand max_eacan change, for example, when you create a new segment.
print(f"min ea = 0x{idaapi.inf_get_min_ea():08x}")
print(f"max ea = 0x{idaapi.inf_get_max_ea():08x}")
# We also have the original values that does not change no matter what
print(f"Original min ea = 0x{idaapi.inf_get_omin_ea():08x}")
print(f"Original max ea = 0x{idaapi.inf_get_omax_ea():08x}")

print(f"String Prefix = \"{idaapi.inf_get_strlit_pref()}\"")
print(f"Carousel Data Type bits = 0x{idaapi.inf_get_datatypes():x}")

## Compiler options
print("IS COMPILED WITH GNU : ", ida_ida.inf_get_cc_id() == ida_typeinf.COMP_GNU)

## Writing to Notepad
ida_nalt.set_ida_notepad_text("Testing AAA")

# Creation Time
print(f'Creation Time : {time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ida_nalt.get_idb_ctime()))}')

# Get Image Base
print(f"Image base is : 0x{idaapi.get_imagebase():x}")
