import ida_kernwin

class MyChoose(ida_kernwin.Choose):
    def __init__(self, title, /,n=12, nb=5, flags = 0, embedded = False, width=None, height=None):
        super().__init__(
            title, 
            [["Address",10],["Name",30],["Type",8]],
            embedded=embedded,
            flags = flags| ida_kernwin.Choose.CH_RESTORE,
            width=width ,
            height=height)
        # These are what you would see when you right click on am entry
        self.popup_names = ["Inzert","Del leet","Ehdeet", "Ree frech"]
        print("Created %s"%str(self))
        self.data = [["0x%x"%(0x401000 + i*10),"Name %d"%i, "Type %d"%i ] for i in range(n)]
    def OnGetSize(self):
        n = len(self.data)
        print("getsize -> %d"%n)
        return n
    def OnGetLine(self, n):
        return self.data[n]
        
    
    def OnDeleteLine(self, sel):
        """
        User deleted an element

        @param sel the current selection
        @return a tuple (changed, selection)
        """
        print("OnDeleteLine : sel = %d"%sel)
        del self.data[sel]
        return (ida_kernwin.Choose.ALL_CHANGED, self.adjust_last_item(sel))
        

    def OnGetIcon(self, n):
        """
        Get an icon to associate with the first cell of an element
        @param n index of the element
        @return an icon ID
        """
        return n + 1
        
        
    def OnGetLineAttr(self, n):
        """
        Get attributes for an element
        @param n index of the element
        @return a tuple (color, flags)
        """
        if n< 10:
            if n%2 == 0:
            
                return [0xff0000,ida_kernwin.CHITEM_BOLD]
            else:
                return [0x0000ff,ida_kernwin.CHITEM_UNDER]
        return (0xffffff,0)
        
mychoose = MyChoose("My Choose",n=900)
r=mychoose.Show(modal=True)
print("dialog returned =%d" %r)