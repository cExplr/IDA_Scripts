import ida_ida
import ida_dbg
import ida_kernwin
import ida_funcs
"""
Taken from dbg_trace.py
"""

ida_dbg.set_debugger_options(ida_dbg.DOPT_TEMP_HWBPT|ida_dbg.DOPT_FAST_STEP)

if ida_ida.inf_get_filetype() == ida_ida.f_PE:
    ida_dbg.load_debugger("win32", 0)
elif ida_ida.inf_get_filetype() == ida_ida.f_ELF:
    ida_dbg.load_debugger("linux", 0)
elif ida_ida.inf_get_filetype() == ida_ida.f_MACHO:
    ida_dbg.load_debugger("mac", 0)
    
state = ida_dbg.get_process_state() 
match state:
    case ida_dbg.DSTATE_NOTASK:
        print("No task running at the moment")
        # Start Debugger process
        executable_path = ""
        args = ""
        starting_dir= "" 
        #ida_dbg.start_process()
        #ida_dbg.run_to(ida_kernwin.get_screen_ea())
        
        ### Run to main function
        main_addr = ida_ida.inf_get_main()
        if main_addr == idaapi.BADADDR:
            print("There is no main function address found ")
            start_ea = ida_ida.inf_get_start_ea()
            ida_dbg.run_to(start_ea)
        else:
            print(f"Main function found at {hex(main_addr)}.\nRunning To Main ...")
            ida_dbg.run_to(main_addr)
        
        
    case ida_dbg.DSTATE_RUN:
        print("Debugger is currently running")
    case ida_dbg.DSTATE_SUSP:
        print("Debugger is currently suspended")