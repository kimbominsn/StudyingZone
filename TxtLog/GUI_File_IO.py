import threading
import tkinter as tk
from tkinter import Spinbox, ttk, scrolledtext, Menu
from tkinter import messagebox as msg
from time import sleep
from threading import Thread
from queue import Queue
from FileOpen import Logging    #FileOpen.py



fileTypes=['txt','hwp','xlsx', 'docx']
class IO_MAIN():
    def __init__(self):
        self.win=tk.Tk()
        self.win.title("File write test")
        self.FileTypesIdx=0                     #default Idx : txt
        self.src_queue=Queue()                  #queue for gui log
        self.logFile=Logging(self.src_queue)
        self.log_stop=threading.Event()         #thread stop flag
        self.create_widgets()

        
    
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
            , args=[self.src_queue, self.log_stop, fileTypes[self.FileTypesIdx]]
        )
        log.start()


    #------------------------ Log stop flag set ---------------------------------
    def action_stop_logging(self):
        self.log_stop.set()
    
    #------------------------ GUI Log clear ---------------------------------
    def action_clear(self):
        pass    #TBD

    def file_type_selection(self):
        self.FileTypesIdx=self.radVar.get()

    #------------------------ Widget Layout ---------------------------------
    def create_widgets(self):

        #------------------------ Tab control ---------------------------------
        tabControl=ttk.Notebook(self.win)    #tab control

        #------------------------ Add tab ---------------------------------
        self.tab1=ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Test Log')
        tabControl.pack(expand=1, fill="both")

        self.tab1_frame=ttk.LabelFrame(self.tab1, text='Frame')
        self.tab1_frame.grid(
            column=0
            , row=0
            , padx=8
            , pady=4
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

        self.btn_clear=ttk.Button(
            self.tab1_frame
            , text= 'Clear All'
            , command=self.action_clear
        )

        self.btn_clear.grid(
            column=2
            , row=0
        )

        #radio btn : 파일 확장자 선택

        self.radFrame=tk.LabelFrame(
            self.tab1
            , text='File type selection'
        )

        self.radFrame.grid(
            column=1
            ,row=0
            ,padx=3
            ,pady=3
            , sticky=tk.N
        )
        
        self.radVar=tk.IntVar()
        self.radVar.set(self.FileTypesIdx)

        for idx in range(len(fileTypes)):
            self.curRad=tk.Radiobutton(
                self.radFrame
                , text=fileTypes[idx]
                , variable=self.radVar
                , value= idx
                , command= self.file_type_selection
            )
            self.curRad.grid(
                column=0
                , row=idx
                , sticky=tk.W
            )




        #scrolled box
        scr_w=50
        scr_h=50

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


#------------------------ Start GUI ---------------------------------
main=IO_MAIN()
main.win.mainloop()