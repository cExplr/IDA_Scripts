import ida_gdl

fn = r"c:\users\cexpl\desktop\x.gdl"

f = ida_funcs.get_func(ida_kernwin.get_screen_ea())
print(f)



ok = idaapi.gen_complex_call_chart(fn, "Computing...","Test Graph", f.start_ea, f.end_ea, idaapi.CHART_RECURSIVE|idaapi.CHART_GEN_GDL | idaapi.CHART_REFERENCING)

if ok :
    print("Success!")
    idaapi.display_gdl(fn)
else:
    print("Failed")
    
    
