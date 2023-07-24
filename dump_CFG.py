import ida_kernwin
import ida_xref
import ida_funcs
import ida_gdl

def ppred(start,end):
    print("\t[^] Pred: [%x - %x"%(start,end) )

def psucc(start,end):
    print("\t[v] Succ : %x - %x"%(start,end) )
    
def hprint(id,start,end):
    print("[*] %x : %x - %x"%(id,start,end))
def using_FlowChart(ea):
    
    pred = []
    succ = []
    
    f = ida_gdl.FlowChart(ida_funcs.get_func(ea))
    print("There are %d basic blocks in this function %s"%(f.size,ida_funcs.get_func_name(ea)))
    print(type(f))
    
    for basicBlock in f:
        hprint(basicBlock.id, basicBlock.start_ea, basicBlock.end_ea)
        for succ_block in basicBlock.succs():
            psucc(succ_block.start_ea, succ_block.end_ea)
        for pred_block in basicBlock.preds():
            ppred(pred_block.start_ea, pred_block.end_ea)
    

ea = ida_kernwin.get_screen_ea()
using_FlowChart(ea)