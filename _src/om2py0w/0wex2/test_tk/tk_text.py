from Tkinter import *

root = Tk()

scroll = Scrollbar(root)
text = Text(root, height=4, width=50)
scroll.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT, fill=Y)

scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished.HAMLET: 
To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
text.insert(END, quote)

root.mainloop()