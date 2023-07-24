import ida_gdl, ida_funcs, ida_kernwin


filename = 'C:\\users\\cexpl\\desktop\\simple_callgraph.gdl'
title = 'Complex Call Graph'

f = ida_funcs.get_func(ida_kernwin.get_screen_ea())

result =  ida_gdl.gen_simple_call_chart(filename, "Building...", title,ida_gdl.CHART_GEN_GDL)

if result:
    print("Ok ...")
    ida_gdl.display_gdl(filename)
else:
    print("Failed...")