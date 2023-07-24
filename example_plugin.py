import idaapi

class hello_plugmod_t(idaapi.plugmod_t):
    def run(self, arg):
        print("hello world! (py)")
        return 0


class hello_plugin_t(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL | idaapi.PLUGIN_MULTI
    comment = "This is a comment"
    help= "This is help"
    wanted_name = 'Hello Python plugin'
    wanted_hotkey = "Alt-F11"
    
    def init(self):
        return hello_plugmod_t()
        pass
    
    def run(self,arg):
        pass
    def term(self):
        pass