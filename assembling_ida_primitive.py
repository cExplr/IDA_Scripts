import ida_idp, idc

# Assemble and get back the bytes.
ida_idp.AssembleLine(idc.here(),0,idc.here(),1,"inc eax")

# Assemble and patch the bytes after testing it.
ida_idp.assemble(idc.here(),0,idc.here(),1,"inc eax")