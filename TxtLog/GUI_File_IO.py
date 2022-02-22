import threading
import tkinter as tk
from tkinter import Listbox, Spinbox, StringVar, ttk, scrolledtext, Menu
from tkinter import messagebox as msg
from threading import Thread
from queue import Queue
from FileOpen import Logging    #FileOpen.py

from tkinter import filedialog as fd
import os

fileTypes=['txt','hwp','xlsx', 'docx']
class IO_MAIN():
    def __init__(self):
        
        
        self.win=tk.Tk()
        self.win.title("File write test")
        self.initialize_variables()             #Log file directory.. set to default test folder
        self.create_widgets()
        self.set_default_value_for_widgets()
        self.src_queue=Queue()                  #queue for gui log
        self.logFile=Logging(self.src_queue, self.fDir, fileTypes[self.FileTypesIdx])
        self.log_stop=threading.Event()         #thread stop flag

        

        
    
    def print_queue_messages(self, log_stop):
        
        while True:
            self.scrBox.insert(
                tk.INSERT
                ,self.src_queue.get()
            )
            if not log_stop:
                break

    #------------------------ Create threads for logging ---------------------------------
    def action_start_logging(self):
        self.log_stop.clear()   #initiate thread event flag
        # Thead for log messages on scrolled box
        src_log=Thread(
            target=self.print_queue_messages
            , daemon=True
            , args=[self.log_stop]
        )
        src_log.start()
        
        # Thread for log files
        log=Thread(
            target=self.logFile.start_logging
            , daemon=True
            , args=[self.src_queue, self.log_stop]
        )
        log.start()


    #------------------------ Log stop flag set ---------------------------------
    def action_stop_logging(self):
        self.log_stop.set()
    
    #------------------------ GUI Log clear ---------------------------------
    def action_clear(self):
        pass    #TBD
        

    def action_view_all(self):
        file_list=os.listdir(self.fDir)
        # print(file_list)
        # print(file_list.count(file_list))
        # count=0
        self.list_cnt.set("List count :"+str(len(file_list)))
        self.list_File.delete(0, tk.END)
        for idx in range(len(file_list)):
            self.list_File.insert(idx, file_list[idx])

        # self.list_File.pack()

    def action_browse(self):
        # fDir=path.dirname(__file__)

        # fName=fd.askopenfilename(parent=self.win, initialdir=self.fDir)
        self.fDir=fd.askdirectory(parent=self.win, initialdir=self.fDir)
        self.txt_fDir.delete(0,tk.END)
        self.txt_fDir.insert(0,self.fDir)
        self.logFile.log_fDir(self.fDir)

    def list_clicked(self, event):
        self.txt_result.delete(0,tk.END)

        lines=self.logFile.log_read(self.list_File.get(self.list_File.curselection()[0]))

        if lines:
            for line in lines:
                self.txt_result.insert(tk.INSERT, line)
        else:
            self.txt_result.insert(tk.INSERT, 'not supported file type')


        # self.txt_result.insert(tk.END,self.list_File.curselection() )

    def file_type_selection(self):
        self.FileTypesIdx=self.radVar.get()
        self.logFile.log_ftype(fileTypes[self.FileTypesIdx])

    def initialize_variables(self):         #must be called before widgets created
        self.fDir="c:/TestDir"
        self.FileTypesIdx=0                 #default Idx : txt
        self.radVar=tk.IntVar()
        self.list_cnt=tk.StringVar()                    
        # self.txt_fDir.delete(0,tk.END)
        # self.txt_fDir.insert(0,self.fDir)
        

    def set_default_value_for_widgets(self):    #call it after creating widgets
        self.radVar.set(self.FileTypesIdx)  #File type selection radio btn : txt
        self.txt_fDir.delete(0,tk.END)
        self.txt_fDir.insert(0,self.fDir)
        


    #------------------------ Widget Layout ---------------------------------
    def create_widgets(self):

        #------------------------ Tab control ---------------------------------
        tabControl=ttk.Notebook(self.win)    #tab control

        #------------------------ Add tab ---------------------------------
        self.tab1=ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Test Log')
        tabControl.pack(expand=1, fill="both")


        #
        self.file_frame=ttk.LabelFrame(self.tab1, text='File Browse')
        self.file_frame.grid(
            column=0
            ,row=0
            , sticky=tk.W
        )

        self.btn_browse=ttk.Button(
            self.file_frame
            , text= 'browse..'
            , command= self.action_browse
        )
        self.btn_browse.grid(
            column=0
            , row=0
        )

        self.txt_fDir=ttk.Entry(
            self.file_frame
            ,width=30
            # ,height=5
            , textvariable=self.fDir
        )

        self.txt_fDir.grid(
            column=1
            , row=0
        )

        #radio btn : 파일 확장자 선택

        self.radFrame=tk.LabelFrame(
            self.tab1
            , text='File type selection'
        )

        self.radFrame.grid(
            column=0
            ,row=1
            ,padx=3
            ,pady=3
            , sticky=tk.W
        )
        
        

        for idx in range(len(fileTypes)):
            self.curRad=tk.Radiobutton(
                self.radFrame
                , text=fileTypes[idx]
                , variable=self.radVar
                , value= idx
                , command= self.file_type_selection
            )
            self.curRad.grid(
                column=idx
                , row=0
                , sticky=tk.W
            )


        self.tab1_frame=ttk.LabelFrame(self.tab1, text='Logging..')
        self.tab1_frame.grid(
            column=0
            , row=2
            , padx=8
            , pady=4
            # , rowspan=2
        )

        #------------------------ Add GUI Widgets ---------------------------------
        self.btn_start=ttk.Button(
            self.tab1_frame
            , text= 'Start Logging'
            , command= self.action_start_logging
        )

        self.btn_start.grid(
            column=0
            , row=0
        )

        self.btn_stop=ttk.Button(
            self.tab1_frame
            , text= 'Stop Logging'
            , command=self.action_stop_logging
        )

        self.btn_stop.grid(
            column=1
            , row=0
        )

        self.btn_view=ttk.Button(
            self.tab1_frame
            , text= 'View All'
            , command=self.action_view_all
        )

        self.btn_view.grid(
            column=2
            , row=0
        )

        #scrolled box for printing queue messages
        scr_w=50
        scr_h=30

        self.scrBox=scrolledtext.ScrolledText(
            self.tab1_frame
            , width= scr_w
            , height=scr_h
            , wrap=tk.WORD
        )

        self.scrBox.grid(
            column=0
            ,row=2
            ,columnspan=3
            ,sticky=tk.EW
        )

        #listbox for lists in fdir
        self.list_File=tk.Listbox(
            self.tab1
            , width= 40
            # , 
        )

        self.list_File.grid(
            column=1
            , row=2
            # , rowspan=3
            , sticky=tk.NS
            , padx=8
            , pady=8
        )

        self.list_File.bind('<<ListboxSelect>>', self.list_clicked)

        self.txt_list_cnt=ttk.Label(
            self.tab1
            ,textvariable=self.list_cnt
        )
        self.txt_list_cnt.grid(
            sticky=tk.SE
            , column=1
            , row=3

        )

        self.txt_result=ttk.Entry(
            self.tab1
            ,width=10
            # ,height=3
        

        )
        self.txt_result.grid(
            column=1
            ,row=0
            , rowspan=2
            , padx=3
            , pady=3
            , sticky=tk.EW

        )



#------------------------ Start GUI ---------------------------------
main=IO_MAIN()
main.win.mainloop()