from textwrap import wrap
import tkinter as tk
from tkinter import W, Spinbox, ttk, scrolledtext, Menu
from tkinter import messagebox as msg
from time import sleep
class ToolTip(object):
    def __init__(self, widget, tip_text=None):
        self.widget=widget
        self.tip_text=tip_text
        widget.bind('<Enter>', self.mouse_enter)
        widget.bind('<Leave>', self.mouse_leave)

    def mouse_enter(self, _event):
        self.show_tooltip()

    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        if self.tip_text:
            x_left=self.widget.winfo_rootx()
            y_top=self.widget.winfo_rooty() -18
            self.tip_window=tk.Toplevel(self.widget)
            self.tip_window.overrideredirect(True)
            self.tip_window.geometry("+%d+%d" % (x_left,y_top))
            label=tk.Label(
                self.tip_window
                , text=self.tip_text
                , justify=tk.LEFT
                , background="#FFFFe0"
                , relief=tk.SOLID
                , borderwidth=1
                , font=("tahoma", "8", "normal")
            )
            label.pack(ipadx=1)

    def hide_tooltip(self):
        if self.tip_text:
            self.tip_window.destroy()





win=tk.Tk()

win.title("Python GUI")
win.iconbitmap('zzang.ico') #상대경로



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

    btn_click.configure(
        text='Hello!'+name.get()+number.get()
    )

btn_click=ttk.Button(
    tab1_frame
    , text='Click Me!'
    , command=clicked
)

btn_click.grid(
    column=2
    ,row=1
)

def _spin():
    value=spin.get()
    print(value)
    scrBox.insert(tk.INSERT, value+'\n')

spin=Spinbox(
    tab1_frame
    # , from_=0
    # , to=10
    , values=(1,11,12,23,34,55,100)
    ,width=5
    , bd=8
    , command= _spin
)

spin.grid(
    column=0
    , row=2
)

ToolTip(spin, 'This is a Spin control')
# def _spin2():
#     value=spin2.get()
#     print(value)
#     scrBox.insert(tk.INSERT, value+'\n')

# spin2=Spinbox(
#     tab1_frame
#     # , from_=0
#     # , to=10
#     , values=(1,11,12,23,34,55,100)
#     ,width=5
#     , bd=9
#     , command= _spin2
#     , relief=tk.RIDGE
# )
# spin2.grid(
#     column=1
#     ,row=2
# )

#scrolled box
scr_w=30
scr_h=3

scrBox=scrolledtext.ScrolledText(
    tab1_frame
    , width= scr_w
    , height=scr_h
    , wrap=tk.WORD
)

scrBox.grid(
    column=0
    # ,row=2
    ,columnspan=3
    ,sticky=tk.EW
)

ToolTip(scrBox, 'This is a ScrolledText widget')

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


#####progress bar#########
progress_bar=ttk.Progressbar(
    tab2
    , orient='horizontal'
    , length=286
    , mode='determinate'
)

progress_bar.grid(
    column=0
    , row=3
    , pady=2
)

def run_progressbar():
    progress_bar['maximum']=100
    for i in range(101):
        sleep(0.05)
        progress_bar['value']=i
        progress_bar.update()
    progress_bar['value']=0

def start_progressbar():
    progress_bar.start()

def stop_progressbar():
    progress_bar.stop()

def progressbar_stop_after(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop)

btn_frame=ttk.LabelFrame(
    tab2_frame
    , text='ProgressBar '
)
btn_frame.grid(
    column=0
    , row=2
    , columnspan=2
    , sticky=tk.W
)

ttk.Button(
    btn_frame
    , text=" Run ProgressBar "
    , command=run_progressbar
).grid(
    column=0
    , row=0
)

ttk.Button(
    btn_frame
    , text=" Start ProgressBar "
    , command=start_progressbar
).grid(
    column=0
    , row=1
)

ttk.Button(
    btn_frame
    , text=" Stop ProgressBar "
    , command=stop_progressbar
).grid(
    column=0
    , row=2
)

ttk.Button(
    btn_frame
    , text=" Stop after second"
    , command=progressbar_stop_after
).grid(
    column=0
    , row=3
)
# num_label=3
# for n in range(num_label):
#     ttk.Label(
#         btn_frame
#         , text=f"label{n}"
#     ).grid(
#         column=n
#         ,row=0
#         ,sticky=tk.W
#     )

for child in btn_frame.winfo_children():
    child.grid_configure(
        padx=2
        ,pady=2
        , sticky=tk.W
    )

for child in tab2.winfo_children():
    child.grid_configure(
        padx=8
        , pady=2
    )

name_entered.focus()
win.mainloop()