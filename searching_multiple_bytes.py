import ida_bytes
import ida_ida
import ida_kernwin
import idaapi

end_ea = ida_ida.inf_get_max_ea()
ea = idaapi.inf_get_min_ea()

text_pattern1 = "50 00 72 ?? ?? ?? 64 00 "
text_pattern2 = "50 00"
pattern = idaapi.compiled_binpat_vec_t()

result = ida_bytes.parse_binpat_str(pattern,ida_ida.inf_get_start_ea(),text_pattern1,16,ida_bytes.PBSENC_DEF1BPU)
result2 = ida_bytes.parse_binpat_str(pattern,ida_ida.inf_get_start_ea(),text_pattern2,16,ida_bytes.PBSENC_DEF1BPU)

# Note that there can be multiple patterns being parsed so we need to account for all the bytes
pattern_length = sum(len(pat.bytes) for pat in pattern)



count = 0
if result == None:
    print("Failed to Compile")
else:
    print("Compiled Ok")
    while True:
        result = ida_bytes.bin_search(ea, end_ea, pattern, ida_bytes.BIN_SEARCH_CASE)
        if result != idaapi.BADADDR:
            #ida_kernwin.jumpto(result)
            print(f"Found Byte Pattern {text_pattern} @ {result:08x}")
            count += 1
        else:
            break
        ea = result + pattern_length # Note that there can be multiple patterns being parsed so we need to account for all the bytes
    print(f"\nTotal Count : {count}\nDone")