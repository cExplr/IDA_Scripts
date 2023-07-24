import idautils
import idaapi

tally = {}

for func_ea in idautils.Functions():
    c =0
    for xb in idautils.XrefsTo(func_ea):
        if xb.iscode: c+= 1
    if c > 0 :
        tally[func_ea] = c

sorted_tally = sorted(tally.items(), key=lambda x: x[1])
sorted_tally =reversed(sorted_tally)

for rank, (func_ea, called_count) in enumerate(sorted_tally):
    print(f"#{rank} {func_ea:16x} {idaapi.get_name(func_ea)} --> {called_count}")