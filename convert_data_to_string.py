## This will attempt to delete ( got to undefine ourselves most of the time) before creating string literal again. Flags has been laid in the comments.

import ida_bytes
import ida_nalt
import ida_kernwin

"""
Different kinds of string types
#define STRTYPE_TERMCHR   (STRWIDTH_1B|STRLYT_TERMCHR<<STRLYT_SHIFT)///< C-style string.
#define STRTYPE_C         STRTYPE_TERMCHR///< Zero-terminated 16bit chars
#define STRTYPE_C_16      (STRWIDTH_2B|STRLYT_TERMCHR<<STRLYT_SHIFT)///< Zero-terminated 32bit chars
#define STRTYPE_C_32      (STRWIDTH_4B|STRLYT_TERMCHR<<STRLYT_SHIFT)///< Pascal-style, one-byte length prefix
#define STRTYPE_PASCAL    (STRWIDTH_1B|STRLYT_PASCAL1<<STRLYT_SHIFT)///< Pascal-style, 16bit chars, one-byte length prefix
#define STRTYPE_PASCAL_16 (STRWIDTH_2B|STRLYT_PASCAL1<<STRLYT_SHIFT)///< Pascal-style, two-byte length prefix
#define STRTYPE_LEN2      (STRWIDTH_1B|STRLYT_PASCAL2<<STRLYT_SHIFT)///< Pascal-style, 16bit chars, two-byte length prefix
#define STRTYPE_LEN2_16   (STRWIDTH_2B|STRLYT_PASCAL2<<STRLYT_SHIFT)///< Pascal-style, four-byte length prefix
#define STRTYPE_LEN4      (STRWIDTH_1B|STRLYT_PASCAL4<<STRLYT_SHIFT)///< Pascal-style, 16bit chars, four-byte length prefix
#define STRTYPE_LEN4_16   (STRWIDTH_2B|STRLYT_PASCAL4<<STRLYT_SHIFT)//@}
"""
ea = ida_kernwin.get_screen_ea()

# Delete the item first
ida_bytes.del_items(ea, ida_bytes.DELIT_SIMPLE)

# Create string literal and choosing the encoding
ida_bytes.create_strlit(ea,0,ida_nalt.STRTYPE_TERMCHR)
ida_bytes.create_strlit(ea,0,ida_nalt.STRTYPE_C_16)