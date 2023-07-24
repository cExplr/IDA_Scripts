import ida_gdl
import ida_kernwin


"""

## FLAGS FOR qflow_chart_t

#define FC_PRINT     0x0001 ///< print names (used only by display_flow_chart())
#define FC_NOEXT     0x0002 ///< do not compute external blocks. Use this to prevent jumps leaving the
                            ///< function from appearing in the flow chart. Unless specified, the
                            ///< targets of those outgoing jumps will be present in the flow
                            ///< chart under the form of one-instruction blocks
#define FC_RESERVED  0x0004 // former FC_PREDS
#define FC_APPND     0x0008 ///< multirange flowchart (set by append_to_flowchart)
#define FC_CHKBREAK  0x0010 ///< build_qflow_chart() may be aborted by user
#define FC_CALL_ENDS 0x0020 ///< call instructions terminate basic blocks
#define FC_NOPREDS   0x0040 ///< do not compute predecessor lists
#define FC_OUTLINES  0x0080 ///< include outlined code (with FUNC_OUTLINE)
"""
ea = ida_kernwin.get_screen_ea()
title = "Charty"
pfn = ida_funcs.get_func(ea)


q = ida_gdl.qflow_chart_t(title, pfn, 0 , 0 ,0)

print(f"Number of basic blocks : {q.size()}")

for id in range(q.size()):
    print(f"Block #{id} : {hex(q[id].start_ea)} - {hex(q[id].end_ea)}")
    
    # SUCC
    for s_idx in range(q.nsucc(id)):
        s_id = q.succ(id,s_idx)
        s_bb = q[s_id]
        print(f"SUCC :  {hex(s_bb.start_ea)} - {hex(s_bb.end_ea)}")
        
   # PRED
    for p_idx in range(q.npred(id)):
        p_id = q.pred(id,p_idx)
        p_bb = q[p_id]
        print(f"PRED :  {hex(p_bb.start_ea)} - {hex(p_bb.end_ea)}")
        
print(q.entry())

