# from textwrap import wrap
import tkinter as tk
from tkinter import W, Spinbox, ttk, scrolledtext, Menu
from tkinter import messagebox as msg
from tkinter import filedialog as fd
from time import sleep
from ToolTip import ToolTip
from threading import Thread    #import thread module
from queue import Queue
import Queues as bq
from os import makedirs, path

GLOBAL_CONST=42
fDir=path.dirname(__file__)
netDir=fDir+'Backup'
if not path.exists(netDir):
    makedirs(netDir, exist_ok=True)

class OOP():

    def __init__(self):
        self.win=tk.Tk()
        ToolTip(self.win, 'Hello GUI')

        self.win.title("Python GUI")
        self.win.iconbitmap('zzang.ico') #상대경로
        self.gui_queue=Queue()
        self.create_widgets()
        self.defaultFileEntries()
        
    ############################################### Callback #######################################################

    def clicked(self):

        self.btn_click.configure(
            text='Hello!'+self.name.get()+self.number.get()
        )
        # self.create_thread()
        bq.write_to_scrol(self)
        # self.use_queues()

        # for idx in range(10):
        #     sleep(5)
        #     self.scrBox.insert(tk.INSERT, str(idx) +'\n')

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

    def method_in_a_thread(self, num_of_loops=10):
        # print('Hi, how are you?\n')
        for idx in range(num_of_loops):
            sleep(1)
            self.scrBox.insert(tk.INSERT, f'{self.run_thread.name}'+str(idx)+'\n')
        sleep(1)
        # print('method_in_a_thread():', self.run_thread.is_alive())
   
    def create_thread(self, num=1):
        self.run_thread=Thread(
            target=self.method_in_a_thread
            , args=[num]
            , daemon=True
        )
        # self.run_thread.setDaemon(True) #runtime error 방지
        self.run_thread.start()
        # print(self.run_thread)
        
        write_thread=Thread(
            target=self.use_queues
            , args=[num]
            , daemon=True)
       
        write_thread.start()


    def use_queues(self, loops=5):
        
        while True:
            print(self.gui_queue.get())

    #file browse 버튼 콜백
    def getFileName(self):
        print('hello from getFileName')
        fDir=path.dirname(__file__)
        fName=fd.askopenfilename(parent=self.win, initialdir=fDir)


    def copyFile(self):
        import shutil
        src=self.fileEntry.get()
        file=src.split('/')[-1]
        dst=self.netwEntry.get() + '' + file
        try:
            shutil.copy(src, dst)
            msg.showinfo('Copy File to Network', 'Success: File copied.')
        except FileNotFoundError as err:
            msg.showerror('Copy File to Network', '*** Failed to copy file! ***\n'+str(err))
        except Exception as ex:
            msg.showerror('Copy File to Network', '*** Failed to copy file! ***\n'+str(ex))

    def defaultFileEntries(self):
        self.fileEntry.delete(0, tk.END)
        self.fileEntry.insert(0, fDir)
        if len(fDir) > self.entryLen:
            self.fileEntry.config(
                # width=len(fDir)+3
                width=35
                , status='readonly'
            )
        
        self.netwEntry.delete(0, tk.END)
        self.netwEntry.insert(0,netDir)

        if(len(netDir))>self.entryLen:
            self.netwEntry.config(
                # width=len(netDir)+3
                width=35
                )

    #---------------------- painting GUI main widgets -------------------------#
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
            # , sticky='W'
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
            , width=24
        )
        self.name_entered.grid(
            column=0
            , row=1
        )
        self.name_entered.delete(0, tk.END)
        self.name_entered.insert(0, '< default name >')

        self.number=tk.StringVar()
        self.number_chosen=ttk.Combobox(
            self.tab1_frame
            , textvariable=self.number
            , width=14
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
            , values=(1,2,4,42,100)
            ,width=5
            , bd=9
            , command= self._spin
        )

        self.spin.grid(
            column=0
            , row=2
        )


        for child in self.tab1_frame.winfo_children():
            child.grid_configure(
                padx=8
                , pady=2
                , sticky=tk.W
            )

        #scrolled box
        scr_w=40
        scr_h=10

        self.scrBox=scrolledtext.ScrolledText(
            self.tab1_frame
            , width= scr_w
            , height=scr_h
            , wrap=tk.WORD
        )


        
        self.scrBox.grid(
            column=0
            # ,row=2
            ,columnspan=3
            ,sticky=tk.EW
        )

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

        #-------------File Browse--------------
        self.mngFilesFrame=ttk.LabelFrame(
            self.tab2
            , text=' Manage Files: '
        )

        self.mngFilesFrame.grid(
            column=0
            , row=1
            , sticky=tk.EW
            , padx=10
            , pady=5
        )

        self.lb=ttk.Button(
            self.mngFilesFrame
            , text="Browse to File ..."
            , command= self.getFileName
        )
        self.lb.grid(
            column=0
            , row=0
            , sticky=tk.W
        )

        file=tk.StringVar()
        self.entryLen=scr_w
        self.fileEntry=ttk.Entry(
            self.mngFilesFrame
            , width=self.entryLen
            , textvariable=file    
        )

        self.fileEntry.grid(
            column=1
            , row=0
            , sticky=tk.W
        )

        logDir=tk.StringVar()
        self.netwEntry=ttk.Entry(
            self.mngFilesFrame
            , width=self.entryLen
            , textvariable=logDir
        )

        self.netwEntry.grid(
            column=1
            , row=1
            , sticky=tk.W
        )

        self.cb=ttk.Button(
            self.mngFilesFrame
            , text="Copy File to : "
            , command=self.copyFile
        )

        self.cb.grid(
            column=0
            , row=1
            , sticky= tk.E
        )

        for child in self.mngFilesFrame.winfo_children():
            child.grid_configure( padx=6, pady=6)

        #-------------progress bar--------------
        self.progress_bar=ttk.Progressbar(
            self.tab2
            , orient='horizontal'
            , length=286
            , mode='determinate'
        )

        self.progress_bar.grid(
            column=0
            , row=2
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

        self.using_global()
        print('Global const : ', GLOBAL_CONST)

        # self.name_entered.focus()
        tabControl.select(1)

        ############################################### tooltips #######################################################
        ToolTip(self.name_entered, 'This is a Entry control')

        ToolTip(self.number_chosen, 'This is a Combobox control')

        ToolTip(self.btn_click, 'This is a button control')

        ToolTip(self.spin, 'This is a Spin control')

        ToolTip(self.scrBox, 'This is a ScrolledText widget')



#=============================================
#   Start GUI
#=============================================

oop=OOP()

# run_thread=Thread(target=oop.method_in_a_thread)

oop.win.mainloop()