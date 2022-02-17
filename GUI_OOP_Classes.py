from textwrap import wrap
import tkinter as tk
from tkinter import W, Spinbox, ttk, scrolledtext, Menu
from tkinter import messagebox as msg
from time import sleep

GLOBAL_CONST=42
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


class OOP():

    def __init__(self):
        self.win=tk.Tk()
        ToolTip(
            self.win
            , 'Hello GUI'
        )

        self.win.title("Python GUI")
        self.win.iconbitmap('zzang.ico') #상대경로
        self.create_widgets()

    def clicked(self):

        self.btn_click.configure(
            text='Hello!'+self.name.get()+self.number.get()
        )

    def _spin(self):
        value=self.spin.get()
        print(value)
        self.scrBox.insert(tk.INSERT, value+'\n')

    def label_change(self):
        radSel=self.radVar.get()

        # if radSel==0:win.configure(background=COLORS[0])
        # elif radSel==1:win.configure(background=COLORS[1])
        # elif radSel==2:win.configure(background=COLORS[2])

        # win.configure(background=COLORS[radSel])
        self.tab2_frame.configure(text=self.COLORS[radSel])

    def run_progressbar(self):
        self.progress_bar['maximum']=100
        for i in range(101):
            sleep(0.05)
            self.progress_bar['value']=i
            self.progress_bar.update()
        self.progress_bar['value']=0

    def start_progressbar(self):
        self.progress_bar.start()

    def stop_progressbar(self):
        self.progress_bar.stop()

    def progressbar_stop_after(self, wait_ms=1000):
        self.win.after(wait_ms, self.progress_bar.stop)

    def using_global(self):
        global GLOBAL_CONST
        print(GLOBAL_CONST)
        GLOBAL_CONST=777
        print(GLOBAL_CONST)

        
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

   

    def create_widgets(self):

        ############################################### Menu #######################################################
        self.menu_bar=Menu(self.win)
        self.win.config(menu=self.menu_bar)

        file_menu=Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)

        self.menu_bar.add_cascade(label="File", menu=file_menu)  #menu "File" drop down

        help_menu=Menu(self.menu_bar, tearoff=0)

        def _msgBox():
            # msg.showinfo('Python Message Info Box', 'A Python GUI created using thkinter:\nThe year is 2022.')
            # msg.showwarning('Python Message Warning Box', 'A Python GUI created using thkinter:\nWarning: There might be a bug in this code.')
            # msg.showerror('Python Message Error Box', 'A Python GUI created using thkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
            answer=msg.askyesnocancel("Python Message Multi Choice Box", "Are you sure you really wish to do this?")
            print(answer)

        help_menu.add_command(label="About", command=_msgBox)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
   
        ############################################### Tab control #######################################################
        tabControl=ttk.Notebook(self.win)    #tab control

        ############################################### Tab1 #######################################################
        self.tab1=ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Tab 1')
        tabControl.pack(expand=1, fill="both")

        self.tab1_frame=ttk.LabelFrame(self.tab1, text='Tab1 Frame')
        self.tab1_frame.grid(
            column=0
            , row=0
            , padx=8
            , pady=4
        )

        self.a_label=ttk.Label(self.tab1_frame, text="Enter a name :")
        self.a_label.grid(
            column=0
            , row=0
            , sticky='W'
        )

        ttk.Label(self.tab1_frame, text='Choose a number:').grid(
            column=1
            ,row=0
        )

        for child in self.tab1_frame.winfo_children():
            child.grid_configure(padx=8)

        self.name=tk.StringVar()
        self.name_entered=ttk.Entry(
            self.tab1_frame
            , text=self.name
            , width=12
        )
        self.name_entered.grid(
            column=0
            , row=1
        )

        self.number=tk.StringVar()
        self.number_chosen=ttk.Combobox(
            self.tab1_frame
            , textvariable=self.number
            , width=12
            , state='readonly'
        )
        self.number_chosen['values']=(1,10,11,15,30,50)
        self.number_chosen.grid(
            column=1
            ,row=1
        )
        self.number_chosen.current(0)

        self.btn_click=ttk.Button(
            self.tab1_frame
            , text='Click Me!'
            , command=self.clicked
        )

        self.btn_click.grid(
            column=2
            ,row=1
        )



        self.spin=Spinbox(
            self.tab1_frame
            # , from_=0
            # , to=10
            , values=(1,11,12,23,34,55,100)
            ,width=5
            , bd=8
            , command= self._spin
        )

        self.spin.grid(
            column=0
            , row=2
        )


        ToolTip(self.spin, 'This is a Spin control')
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

        self.scrBox=scrolledtext.ScrolledText(
            self.tab1_frame
            , width= scr_w
            , height=scr_h
            , wrap=tk.WORD
        )

        for child in self.tab1_frame.winfo_children():
            child.grid_configure(
                padx=8
                , pady=2
            )
        
        self.scrBox.grid(
            column=0
            # ,row=2
            ,columnspan=3
            ,sticky=tk.EW
        )

        ToolTip(self.scrBox, 'This is a ScrolledText widget')

        ############################################### Tab2 #######################################################
        self.tab2=ttk.Frame(tabControl)
        tabControl.add(self.tab2, text='Tab 2')

        self.tab2_frame=ttk.LabelFrame(self.tab2, text='The Snake')
        self.tab2_frame.grid(
            column=0
            , row=0
            , padx=8
            , pady=4
        )

        #-------------check btn --------------
        self.chVarDis=tk.IntVar()    #0:uncheched / 1:checked
        self.chVarUn=tk.IntVar()
        self.chVarEn=tk.IntVar()

        self.ckbtn1=tk.Checkbutton(
            self.tab2_frame
            , text='Disabled'
            , variable=self.chVarDis
            , state=tk.DISABLED
        )
        self.ckbtn1.select()
        self.ckbtn1.grid(
            column=0
            , row=0
        )
        self.ckbtn2=tk.Checkbutton(
            self.tab2_frame
            , text='UnChecked'
            , variable=self.chVarUn
        )
        self.ckbtn2.deselect()
        self.ckbtn2. grid(
            column=1
            ,row=0
        )
        self.ckbtn3=tk.Checkbutton(
            self.tab2_frame
            , text='Enabled'
            , variable=self.chVarEn
        )
        self.ckbtn3. grid(
            column=2
            ,row=0
        )
        self.ckbtn3.select()
        #-------------radio button--------------
        self.COLORS=["Blue","Gold","Red"] #list

        self.radVar=tk.IntVar()
        self.radVar.set(99)

        for n in range(3):
            self.curRad=tk.Radiobutton(
                self.tab2_frame
                ,text=self.COLORS[n]
                , variable=self.radVar
                , value=n
                , command=self.label_change
            ).grid(
                column=n
                ,row=1
            )


        #-------------progress bar--------------
        self.progress_bar=ttk.Progressbar(
            self.tab2
            , orient='horizontal'
            , length=286
            , mode='determinate'
        )

        self.progress_bar.grid(
            column=0
            , row=3
            , pady=2
        )

        self.btn_frame=ttk.LabelFrame(
            self.tab2_frame
            , text='ProgressBar '
        )
        self.btn_frame.grid(
            column=0
            , row=2
            , columnspan=2
            , sticky=tk.W
        )

        ttk.Button(
            self.btn_frame
            , text=" Run ProgressBar "
            , command=self.run_progressbar
        ).grid(
            column=0
            , row=0
        )

        ttk.Button(
            self.btn_frame
            , text=" Start ProgressBar "
            , command=self.start_progressbar
        ).grid(
            column=0
            , row=1
        )

        ttk.Button(
            self.btn_frame
            , text=" Stop ProgressBar "
            , command=self.stop_progressbar
        ).grid(
            column=0
            , row=2
        )

        ttk.Button(
            self.btn_frame
            , text=" Stop after second"
            , command=self.progressbar_stop_after
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

        for child in self.btn_frame.winfo_children():
            child.grid_configure(
                padx=2
                ,pady=2
                , sticky=tk.W
            )

        for child in self.tab2_frame.winfo_children():
            child.grid_configure(
                padx=8
                , pady=2
            )

        ############################################### Tab3 #######################################################
        self.tab3=ttk.Frame(tabControl)
        tabControl.add(self.tab3, text='Tab 3')

        tab3_frame=tk.Frame(self.tab3, bg='blue')
        tab3_frame.pack()
        for orange_color in range(2):
            self.canvas = tk.Canvas(
                tab3_frame
                ,width=150
                ,height=80
                ,highlightthickness=0
                ,bg='orange'
            )
            self.canvas.grid(
                row=orange_color
                ,column=orange_color
            )


        # strData=spin.get()
        # print("AAA Spinbox value:"+strData)

        self.using_global()
        print('Global const : ', GLOBAL_CONST)

        self.name_entered.focus()

oop=OOP()
oop.win.mainloop()