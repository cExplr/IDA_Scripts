"""
IDAPython Script to highlight function calls.
Re-implemented by jthuraisamy (not the original author).

Install to %IDADIR%\plugins\highlight_calls.py.

Run by pressing Ctrl+Alt+H or go to Options -> Highlight Call Instructions.
"""
import idaapi
import ida_kernwin
import idautils
import idc

class HighlightHandler(idaapi.action_handler_t):
    def __init__(self):
        idaapi.action_handler_t.__init__(self)

    # Say hello when invoked.
    def activate(self, ctx):
        hc = highlight_calls_plugin_t()
        hc.run(ctx)
        return 1

    # This action is always available.
    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS

class highlight_calls_plugin_t(idaapi.plugin_t):
	flags = idaapi.PLUGIN_KEEP
	comment = 'Highlight Function Calls'

	help = ''
	wanted_name = 'Highlight Call Instructions'
	wanted_hotkey = 'Ctrl+Alt+H'

	def init(self):
		# Register action.
		action_desc = idaapi.action_desc_t(
			'hc:hc',
			'(Un)Highlight Call Instructions',
			HighlightHandler(),
			None, # Keyboard shortcut.
			'Highlights call instructions.')

		# Populate action menu.
		ida_kernwin.register_action(action_desc)
		ida_kernwin.attach_action_to_menu(
			'Options/',
			'hc:hc',
			idaapi.SETMENU_APP)

		return idaapi.PLUGIN_KEEP

	def term(self):
		ida_kernwin.detach_action_from_menu('Options/', 'hc:hc')
		ida_kernwin.unregister_action('hc:hc')
		return None

	def run(self, arg):
		self.highlight_calls()

	def highlight_calls(self, color=0xCCFFFF): # Light Yellow
	    for ea in idautils.Heads():
	        if idaapi.is_code(idaapi.get_flags(ea)) and idaapi.is_call_insn(ea):
	            current_color = idaapi.get_item_color(ea)
	            if current_color == color:
	                idaapi.set_item_color(ea, idc.DEFCOLOR)
	            elif current_color == idc.DEFCOLOR:
	                idaapi.set_item_color(ea, color)

def PLUGIN_ENTRY():
	return highlight_calls_plugin_t()