from Tkinter import *

class LabelEntry(Frame):
    def __init__(self, parent, title, **config):
        Frame.__init__(self, parent, **config)
        self.title = title
        self.user_input = StringVar(parent)
        self.pack()
        self.makeWidgets()


    def makeWidgets(self):
        Label(self, text=self.title).pack(side=LEFT)
        ent = Entry(self, textvariable=self.user_input)
        ent.pack(side=RIGHT)
        ent.bind('<Return>', self.onReturnKey)

    def onReturnKey(self, event):
        print(self.user_input.get())

if __name__ == '__main__':
    tkroot = Tk()
    widget = LabelEntry(tkroot, 'corp_title')
    widget.mainloop()
