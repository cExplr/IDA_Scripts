import ida_gdl
import ida_funcs
import ida_kernwin

title = "test gdl"
filename = "C:\\users\\cexpl\\desktop\\test.gdl"

f = ida_funcs.get_func(ida_kernwin.get_screen_ea())

gen_result = ida_gdl.gen_flow_graph(filename, title, f, f.start_ea, f.end_ea, ida_gdl.CHART_GEN_GDL)

if gen_result:
    
    print("Done. File stroed in %s"%(filename))
    ida_gdl.display_gdl(filename)
else:
    print("Failed")