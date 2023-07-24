import ida_idd
import ida_bytes

"""
////// \defgroup BIN_SEARCH_ Search flags
/// passed as 'flags' parameter to bin_search()
//@{
#define BIN_SEARCH_CASE         0x01 ///< case sensitive
#define BIN_SEARCH_NOCASE       0x00 ///< case insensitive#define BIN_SEARCH_NOBREAK      0x02 ///< don't check for Ctrl-Break
#define BIN_SEARCH_INITED       0x04 ///< find_byte, find_byter: any initilized value
#define BIN_SEARCH_NOSHOW       0x08 ///< don't show search progress or update screen
#define BIN_SEARCH_FORWARD      0x00 ///< search forward for bytes
#define BIN_SEARCH_BACKWARD     0x10 ///< search backward for bytes
#define BIN_SEARCH_BITMASK      0x20 ///< searching using strict bit mask//@}

## Example:
ea = ida_bytes.bin_search(
                    current_ea,
                    ida_ida.inf_get_max_ea(),
                    patterns,
                    ida_bytes.BIN_SEARCH_FORWARD
                  | ida_bytes.BIN_SEARCH_NOBREAK
                  | ida_bytes.BIN_SEARCH_NOSHOW)

"""
byte_to_find = 0x50

min_ea = ida_ida.inf_get_min_ea()
max_ea = ida_ida.inf_get_max_ea()

while True:
    min_ea = ida_bytes.find_byte(
            min_ea ,
            max_ea - min_ea ,byte_to_find,ida_bytes.BIN_SEARCH_NOCASE|ida_bytes.BIN_SEARCH_NOBREAK|ida_bytes.BIN_SEARCH_NOSHOW)
    if min_ea == idaapi.BADADDR:
        print(f"Byte 0x{byte_to_find:x} not found from 0x{hex(min_ea) } to 0x{hex(min_ea)}")
        break
    else:
        # check if it is both code and is the first byte
        f = ida_bytes.get_flags(min_ea)
        if ida_bytes.is_code(f) and ida_bytes.is_head(f):
            print(f"Byte 0x{byte_to_find:x} found from {hex(min_ea) } to {hex(max_ea) } @ {hex(min_ea)}")
    min_ea += 1
