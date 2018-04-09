import os
import Tkinter
import tkMessageBox

top = Tkinter.Tk()


def helloCallBack():
	os.system('python objdet.py')
        #if count>200:
#		tkMessageBox.showinfo( "error", "error")
#	if count<200:
#		tkMessageBox.showinfo("starting","starting")
B = Tkinter.Button(top, text ="start machine", command = helloCallBack)

B.pack()
top.mainloop()



