import ida_gdl

fn = r"c:\users\cexpl\desktop\x.gdl"

ok = idaapi.gen_flow_graph(fn, "Test Graph", idaapi.get_func(idc.here()), 0 ,0 ,idaapi.CHART_GEN_GDL)

if ok :
    print("Success!")
    idaapi.display_gdl(fn)
else:
    print("Failed")