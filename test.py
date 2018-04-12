import Tkinter as tk
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import Figure
import xlrd
import os
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

root = tk.Tk()
root.geometry("900x700+100+100")
root.configure(background="gray")
def d2():
	os.system('python objdet1.py')
	b = tk.Label(root, text ="starting machine")
        b.place(x=400,y=300)
        w=tk.Label(root,text="stopping if error")
        w.place(x=400,y=350)
def d3():
        os.system('python objdet2.py')
	b = tk.Label(root, text ="starting machine")
        b.place(x=400,y=300)
        w=tk.Label(root,text="stopping if error")
        w.place(x=400,y=350)
def d4():
        os.system('python objdet4.py')
	b = tk.Label(root, text ="starting machine")
        b.place(x=400,y=300)
        w=tk.Label(root,text="stopping if error")
        w.place(x=400,y=350)
def d1():
	os.system('python objdet.py')
#        if count>200:
#		tkMessageBox.showinfo( "error", "error")
#	if count<200:
#		tkMessageBox.showinfo("starting","starting")
	b = tk.Label(root, text ="starting machine")
	b.place(x=400,y=300)
	w=tk.Label(root,text="stopping if error")
	w.place(x=400,y=350)
def v():
	os.system('python videodet.py')
def d():

	button = tk.Button(root, text='Western', width=25,command=d1)
	button.place(x=350,y=100)

	button = tk.Button(root, text='Northern', width=25,command= d2)
	button.place(x=350,y=130)
	
	button = tk.Button(root, text='southern', width=25,command=d3)
	button.place(x=350,y=160)

	button = tk.Button(root, text='northern', width=25,command= d4)
	button.place(x=350,y=190)


def b():

	button = tk.Button(root, text='based_on_persons', width=25,command=a)
	button.place(x=650,y=130)
	#button.pack(pady=30)
	button = tk.Button(root, text='based_on_area', width=25,command= c)
	button.place(x=650,y=150)
	#button.pack(pady=30)

def a():
	#fig = matplotlib.pyplot.Figure()
	f = Figure(figsize=(5,4), dpi=100)
	ax = f.add_subplot(111)


	# create matplotlib canvas using `fig` and assign to widget `top`
	#canvas = FigureCanvasTkAgg(fig,master=root)

	# get canvas as tkinter widget and put in widget `top`
	#canvas.get_tk_widget().place(x=350,y=200)

	# create toolbar               
	#toolbar = NavigationToolbar2TkAgg(canvas,top)
	#toolbar.update()
	#canvas._tkcanvas.pack()
	data1=[]
	for i in range(1,11):
		workbook = xlrd.open_workbook('data1.xlsx')
		worksheet = workbook.sheet_by_index(0)
		data2 = worksheet.cell(i, 0).value
		print data2
		data1.append(data2)
	#data = {
   	# 'Gender':[1, 2, 3,4,5,6,7,8,9,10],
	# 'data1' ,
	#	}

	#df = pd.DataFrame(data)

	#x = 'Gender'
	#y = 'data1'

	#new_df = df[[x, y]].groupby(x).sum()

# create first place for plot
	#ax = fig.add_subplot(111)

# draw on this plot
	#new_df.plot(kind='bar', legend=False, ax=ax)

	ind = (1532,1533,1534,1535,1536,1537,1538,1539,1540,1541)  # the x locations for the groups
	width = .4
	print data1
	rects1 = ax.bar(ind , data1 , width)
	canvas = FigureCanvasTkAgg(f, master=root)
	canvas.show()
	canvas.get_tk_widget().place(x=350,y=250)

def c():
	f = Figure(figsize=(5,4), dpi=100)
	ax = f.add_subplot(111)
	data1=[]
        for i in range(1,5):
                workbook = xlrd.open_workbook('data1.xlsx')
                worksheet = workbook.sheet_by_index(0)
                data2 = worksheet.cell(i, 0).value
                print data2
                data1.append(data2)
        #data = {
	ind = ('western','eastern','northern','southern')  # the x locations for the groups
	width = .5
	rects1 = ax.bar(ind, data1, width)
	canvas = FigureCanvasTkAgg(f, master=root)
	canvas.show()
	canvas.get_tk_widget().place(x=350,y=250)


def a1():
	w=tk.Label(root,text="Name : sample_Person_1 ")
	w1=tk.Label(root,text="Age : 38 ")
	w2=tk.Label(root,text="Location : Western ")
	w3=tk.Label(root,text="helmet id : 1532 ")
	w4=tk.Label(root,text="Air Quality level : 1023 ")
	w5=tk.Label(root,text="CV status : no problem ")
	w.place(x=50,y=310)
	w1.place(x=50,y=340)
	w3.place(x=50,y=370)
	w2.place(x=50,y=400)
	w4.place(x=50,y=430)
	w5.place(x=50,y=460)
def a2():
    w=tk.Label(root,text="Name : sample_Person_2 ")
    w1=tk.Label(root,text="Age : 21 ")
    w2=tk.Label(root,text="Location : Eastern ")
    w3=tk.Label(root,text="helmet id : 1533 ")
    w4=tk.Label(root,text="Air Quality level : 1536 ")
    w5=tk.Label(root,text="CV status : no problem ")
    w.place(x=50,y=310)
    w1.place(x=50,y=340)
    w3.place(x=50,y=370)
    w2.place(x=50,y=400)
    w4.place(x=50,y=430)
    w5.place(x=50,y=460)

def a3():
    w=tk.Label(root,text="Name : sample_Person_3 ")
    w1=tk.Label(root,text="Age : 27 ")
    w2=tk.Label(root,text="Location : Western ")
    w3=tk.Label(root,text="helmet id : 1534 ")
    w4=tk.Label(root,text="Air Quality level : 1023 ")
    w5=tk.Label(root,text="CV status : no problem ")
    w.place(x=50,y=310)
    w1.place(x=50,y=340)
    w3.place(x=50,y=370)
    w2.place(x=50,y=400)
    w4.place(x=50,y=430)
    w5.place(x=50,y=460)

def a4():
    w=tk.Label(root,text="Name : sample_Person_4 ")
    w1=tk.Label(root,text="Age : 43 ")
    w2=tk.Label(root,text="Location : southern ")
    w3=tk.Label(root,text="helmet id : 1535 ")
    w4=tk.Label(root,text="Air Quality level : 3223 ")
    w5=tk.Label(root,text="CV status : no problem ")
    w.place(x=50,y=310)
    w1.place(x=50,y=340)
    w3.place(x=50,y=370)
    w2.place(x=50,y=400)
    w4.place(x=50,y=430)
    w5.place(x=50,y=460)

def a5():
    w=tk.Label(root,text="Name : sample_Person_5 ")
    w1=tk.Label(root,text="Age : 38 ")
    w2=tk.Label(root,text="Location : Northern ")
    w3=tk.Label(root,text="helmet id : 1536 ")
    w4=tk.Label(root,text="Air Quality level : 9073 ")
    w5=tk.Label(root,text="CV status : no problem ")
    w.place(x=50,y=310)
    w1.place(x=50,y=340)
    w3.place(x=50,y=370)
    w2.place(x=50,y=400)
    w4.place(x=50,y=430)
    w5.place(x=50,y=460)

def a6():
    w=tk.Label(root,text="Name : sample_Person_7 ")
    w1=tk.Label(root,text="Age : 48 ")
    w2=tk.Label(root,text="Location : Western ")
    w3=tk.Label(root,text="helmet id : 1537 ")
    w4=tk.Label(root,text="Air Quality level : 1023 ")
    w5=tk.Label(root,text="CV status : no problem ")
    w.place(x=500,y=100)
    w1.place(x=500,y=130)
    w3.place(x=500,y=160)
    w2.place(x=500,y=190)
    w4.place(x=500,y=220)
    w5.place(x=500,y=250)

def a7():
    w=tk.Label(root,text="Name : sample_Person_8 ")
    w1=tk.Label(root,text="Age : 23 ")
    w2=tk.Label(root,text="Location : southern ")
    w3=tk.Label(root,text="helmet id : 1538 ")
    w4=tk.Label(root,text="Air Quality level : 3223 ")
    w5=tk.Label(root,text="CV status : no problem ")
    w.place(x=500,y=100)
    w1.place(x=500,y=130)
    w3.place(x=500,y=160)
    w2.place(x=500,y=190)
    w4.place(x=500,y=220)
    w5.place(x=500,y=250)

def a8():
    w=tk.Label(root,text="Name : sample_Person_9 ")
    w1=tk.Label(root,text="Age : 30 ")
    w2=tk.Label(root,text="Location : Northern ")
    w3=tk.Label(root,text="helmet id : 1539 ")
    w4=tk.Label(root,text="Air Quality level : 9073 ")
    w5=tk.Label(root,text="CV status : no problem ")
    w.place(x=500,y=100)
    w1.place(x=500,y=130)
    w3.place(x=500,y=160)
    w2.place(x=500,y=190)
    w4.place(x=500,y=220)
    w5.place(x=500,y=250)

def a9():
    w=tk.Label(root,text="Name : sample_Person_10 ")
    w1=tk.Label(root,text="Age : 41 ")
    w2=tk.Label(root,text="Location : eastern ")
    w3=tk.Label(root,text="helmet id : 1540 ")
    w4=tk.Label(root,text="Air Quality level : 2087 ")
    w5=tk.Label(root,text="CV status : no problem ")
    w.place(x=500,y=100)
    w1.place(x=500,y=130)
    w3.place(x=500,y=160)
    w2.place(x=500,y=190)
    w4.place(x=500,y=220)
    w5.place(x=500,y=250)

def a10():
    w=tk.Label(root,text="Name : sample_Person_6 ")
    w1=tk.Label(root,text="Age : 18 ")
    w2=tk.Label(root,text="Location : Western ")
    w3=tk.Label(root,text="helmet id : 1541 ")
    w4=tk.Label(root,text="Air Quality level : 1023 ")
    w5=tk.Label(root,text="CV status : no problem ")
    w.place(x=500,y=100)
    w1.place(x=500,y=130)
    w3.place(x=500,y=160)
    w2.place(x=500,y=190)
    w4.place(x=500,y=220)
    w5.place(x=500,y=250)


button = tk.Button(root, text='sample_person_1', width=25, command=a1)
button.place(y=100,x=50)

button = tk.Button(root, text='sample_person_2', width=25, command=a2)
button.place(y=140,x=50)

button = tk.Button(root, text='sample_person_3', width=25, command=a3)
button.place(y=180,x=50)

button = tk.Button(root, text='sample_person_4', width=25, command=a4)
button.place(y=220,x=50)

button = tk.Button(root, text='sample_person_5', width=25, command=a5)
button.place(y=260,x=50)

#button = tk.Button(root, text='sample_person_6', width=25, command=a10)
#button.place(y=300,x=50)

#button = tk.Button(root, text='sample_person_7', width=25, command=a6)
#button.place(y=340,x=50)

#button = tk.Button(root, text='sample_person_8', width=25, command=a7)
#button.place(y=380,x=50)

#button = tk.Button(root, text='sample_person_9', width=25, command=a8)
#button.place(y=420,x=50)

#button = tk.Button(root, text='sample_person_10', width=25, command=a9)
#button.place(y=460,x=50)

button = tk.Button(root, text='Air quality detection', width=25,command = b)
button.place(y=520,x=50)

button = tk.Button(root, text='checking cv status', width=25,command = d)
button.place(y=550,x=50)

button = tk.Button(root, text='video detection', width=25,command = v)
button.place(y=600,x=50)


w=tk.Label(root,text="Workers at coal mines")
w.place(x=50,y=50)

root.mainloop()

