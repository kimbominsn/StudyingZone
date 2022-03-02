import tkinter as tk
from tkinter import ttk, scrolledtext, Menu

#tkinter instance생성
win=tk.Tk()
#window title
win.title("Python GUI")

outlayer=ttk.LabelFrame(win, text='My Layout')
outlayer.grid(
    column=0
    ,row=0
    ,padx=8
    ,pady=4
)

a_label=ttk.Label(outlayer,text="Enter your name:")
a_label.grid(
    column=0
    , row=0
    , sticky=tk.W
)

def click_me():
    action.configure(
        text='Hello!'+name.get()+number.get()
    )
    # a_label.configure(foreground='red')
    # a_label.configure(text='A Red Label')
    #name.set(number.get())


#add entrybox
name=tk.StringVar()
name_entered=ttk.Entry(
    outlayer
    ,width=12
    , textvariable=name
)
name_entered.grid(
    column=0
    ,row=1
    , sticky=tk.W
)

#adding btn
action=ttk.Button(
    outlayer
    ,text="Click Me!"
    , command=click_me
)
action.grid(
    column=2
    , row=1
    , sticky=tk.W
)
# action.configure(state='disabled')

ttk.Label(
    outlayer
    ,text="Choose a number:"
    ).grid(
    column=1
    ,row=0
    , sticky=tk.W
)
number=tk.StringVar()
number_chosen=ttk.Combobox(
    outlayer
    ,width=12
    ,textvariable=number
    ,state='readonly'
)
number_chosen['values']=(1,2,4,42,100)
number_chosen.grid(
    column=1
    ,row=1
    , sticky=tk.W
)
number_chosen.current(0)

chVarDis=tk.IntVar()    #0:uncheched / 1:checked
chVarUn=tk.IntVar()
chVarEn=tk.IntVar()

checkB1=tk.Checkbutton(
    outlayer
    , text="Disabled"
    , variable=chVarDis
    , state='disabled'
)
checkB1.grid(
    column=0
    , row=4
    , sticky=tk.W
)  #tk.W : grid 서쪽 정렬
checkB1.select()

checkB2=tk.Checkbutton(
    outlayer
    ,text="Unchecked"
    , variable=chVarUn
)
checkB2.grid(
    column=1
    ,row=4
    , sticky=tk.W
)
checkB2.deselect()

checkB3=tk.Checkbutton(
    outlayer
    ,text="Enabled"
    , variable=chVarEn
)
checkB3.grid(
    column=2
    ,row=4
    , sticky=tk.W
)
checkB3.select()

#color list : https://www.tcl.tk/man/tcl8.5/TkCmd/colors.html
COLORS=["Blue","Gold","Red"] #list

def radCall():
    radSel=radVar.get()
    win.configure(background=COLORS[radSel])
    # if radSel==0:win.configure(background=COLORS[0])
    # elif radSel==1:win.configure(background=COLORS[1])
    # elif radSel==2:win.configure(background=COLORS[2])

radVar=tk.IntVar()

radVar.set(99)  #오작동 방지를 위해 범위 밖 값 세팅

for col in range(3):
    curRad=tk.Radiobutton(
        outlayer
        ,text=COLORS[col]
        , variable=radVar
        , value=col
        , command=radCall
    )
    curRad.grid(
        column=col
        , row=5
        , sticky=tk.W
    )
# rad1=tk.Radiobutton(win,text=COLORS[0], variable=radVar, value=1, command=radCall)
# rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)
# rad2=tk.Radiobutton(win,text=COLORS[1], variable=radVar, value=2, command=radCall)
# rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)
# rad3=tk.Radiobutton(win,text=COLORS[2], variable=radVar, value=3, command=radCall)
# rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

##scrolledText

scrol_w=30
scrol_h=3

scr=scrolledtext.ScrolledText(
    outlayer
    ,width=scrol_w
    ,height=scrol_h
    ,wrap=tk.WORD
)    #tk.WORD : 단어별 줄바꿈
scr.grid(
    column=0
    , row=6
    ,columnspan=3
    ,sticky=tk.EW
)

#LabelFrame

num_btn=3

# buttons_frame=ttk.LabelFrame(win, text='Labels in a Frame')
buttons_frame=ttk.LabelFrame(
    outlayer
    , text='Labels in a Frame'
)
buttons_frame.grid(
    column=0
    , row=7
    # , padx=10
    # , pady=20
    ,columnspan=3
    ,sticky='W'
)

for n in range(num_btn):
    ttk.Label(buttons_frame, text=f"Label{n}").grid(
        column=n
        , row=0
        , sticky=tk.W
    )
    # if n==0:
    #     ttk.Label(buttons_frame, text=f"Lable{n}--sooooomuch loooooooooooonger").grid(column=0, row=n)
    # else:
    #     ttk.Label(buttons_frame, text=f"Label{n}").grid(column=0, row=n, sticky=tk.W, padx=8, pady=4)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

for child in outlayer.winfo_children():
    child.grid_configure(sticky='W')


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
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")
#set focus to entry
name_entered.focus()
#============================
#       Start GUI
#============================
win.mainloop()  #이벤트 순환문 시작



