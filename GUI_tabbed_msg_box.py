from textwrap import wrap
import tkinter as tk
from tkinter import W, ttk, scrolledtext, Menu
from tkinter import messagebox as msg
win=tk.Tk()

win.title("Python GUI")


############################################### Menu #######################################################
menu_bar=Menu(win)
win.config(menu=menu_bar)

def _quit():
    win.quit()
    win.destroy()
    exit()


file_menu=Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)



menu_bar.add_cascade(label="File", menu=file_menu)  #menu 수직정렬

help_menu=Menu(menu_bar, tearoff=0)


def _msgBox():
    # msg.showinfo('Python Message Info Box', 'A Python GUI created using thkinter:\nThe year is 2022.')
    # msg.showwarning('Python Message Warning Box', 'A Python GUI created using thkinter:\nWarning: There might be a bug in this code.')
    # msg.showerror('Python Message Error Box', 'A Python GUI created using thkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
    answer=msg.askyesnocancel("Python Message Multi Choice Box", "Are you sure you really wish to do this?")
    print(answer)

help_menu.add_command(label="About", command=_msgBox)
menu_bar.add_cascade(label="Help", menu=help_menu)

#Tab Control 생성
tabControl=ttk.Notebook(win)    #tab control

############################################### Tab1 #######################################################
tab1=ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.pack(expand=1, fill="both")

tab1_frame=ttk.LabelFrame(tab1, text='mighty python')
tab1_frame.grid(
    column=0
    , row=0
    , padx=8
    , pady=4
)

a_label=ttk.Label(tab1_frame, text="Enter a name :")
a_label.grid(
    column=0
    , row=0
    , sticky='W'
)

ttk.Label(tab1_frame, text='Choose a number:').grid(
    column=1
    ,row=0
)

for child in tab1_frame.winfo_children():
    child.grid_configure(padx=8)

name=tk.StringVar()
name_entered=ttk.Entry(
    tab1_frame
    , text=name
    , width=12
)
name_entered.grid(
    column=0
    , row=1
)

number=tk.StringVar()
number_chosen=ttk.Combobox(
    tab1_frame
    , textvariable=number
    , width=12
    , state='readonly'
)
number_chosen['values']=(1,10,11,15,30,50)
number_chosen.grid(
    column=1
    ,row=1
)
number_chosen.current(0)

def clicked():
    btn_click.configure(text='thanks')

btn_click=ttk.Button(
    tab1_frame
    , text='Click Me!'
    , command=clicked
)

btn_click.grid(
    column=2
    ,row=1
)



#scrolled box
scr_w=30
scr_h=3

scrBox=scrolledtext.ScrolledText(
    tab1_frame
    , width= scr_w
    , height=scr_h
    , wrap=tk.WORD
).grid(
    column=0
    ,row=2
    ,columnspan=3
    ,sticky=tk.EW
)



############################################### Tab2 #######################################################
tab2=ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tab2_frame=ttk.LabelFrame(tab2, text='The Snake')
tab2_frame.grid(
    column=0
    , row=0
    , padx=8
    , pady=4
)

chVarDis=tk.IntVar()    #0:uncheched / 1:checked
chVarUn=tk.IntVar()
chVarEn=tk.IntVar()

chbtn1=tk.Checkbutton(
    tab2_frame
    , text='Disabled'
    , variable=chVarDis
    , state=tk.DISABLED
)
chbtn1.select()
chbtn1.grid(
    column=0
    , row=0
)
chbtn2=tk.Checkbutton(
    tab2_frame
    , text='UnChecked'
    , variable=chVarUn
)
chbtn2.deselect()
chbtn2. grid(
    column=1
    ,row=0
)
chbtn3=tk.Checkbutton(
    tab2_frame
    , text='Enabled'
    , variable=chVarEn
)
chbtn3. grid(
    column=2
    ,row=0
)

chbtn3.select()



COLORS=["Blue","Gold","Red"] #list

def label_change():
    radSel=radVar.get()

    # if radSel==0:win.configure(background=COLORS[0])
    # elif radSel==1:win.configure(background=COLORS[1])
    # elif radSel==2:win.configure(background=COLORS[2])

    # win.configure(background=COLORS[radSel])
    tab2_frame.configure(text=COLORS[radSel])

radVar=tk.IntVar()
radVar.set(99)

for n in range(3):
    curRad=tk.Radiobutton(
        tab2_frame
        ,text=COLORS[n]
        , variable=radVar
        , value=n
        , command=label_change
    ).grid(
        column=n
        ,row=1
    )

in_frame=ttk.LabelFrame(
    tab2_frame
    , text='labels in a Frame'
)
in_frame.grid(
    column=0
    , row=2
    , columnspan=3
)

# ttk.Label(
#     in_frame
#     , text="1"
# ).grid(column=0,row=0)

num_label=3
for n in range(num_label):
    ttk.Label(
        in_frame
        , text=f"label{n}"
    ).grid(
        column=n
        ,row=0
        ,sticky=tk.W
    )

for child in in_frame.winfo_children():
    child.grid_configure(
        padx=8
        ,pady=4
    )

name_entered.focus()
win.mainloop()