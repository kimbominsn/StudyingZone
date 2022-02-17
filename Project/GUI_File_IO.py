import threading
import tkinter as tk
from tkinter import Spinbox, ttk, scrolledtext, Menu
from tkinter import messagebox as msg
from time import sleep
from threading import Thread    #import thread module
from FileOpen import Logging
from queue import Queue

class IO_MAIN():
    def __init__(self):
        self.win=tk.Tk()
        self.win.title("File write test")
        self.create_widgets()
        self.src_queue=Queue()
        self.logFile=Logging(self.src_queue)
        self.log_stop=threading.Event()
        
    
    def use_queues(self, log_stop):
        
        while True:
            # print(self.src_queue.get())
            self.scrBox.insert(
                tk.INSERT
                ,self.src_queue.get()
            )
            if not log_stop:
                break

    #------------------------ Create threads for logging ---------------------------------
    def action_start_logging(self):
        # Thead for log messages on scrolled box
        src_log=Thread(
            target=self.use_queues
            , daemon=True
            , args=[self.log_stop]
        )
        src_log.start()
        
        # Thread for log files
        self.log_stop.clear()   #initiate thread event flag
        log=Thread(
            target=self.logFile.start_logging
            , daemon=True
            , args=[self.src_queue, self.log_stop]
        )
        log.start()


    #------------------------ Log stop flag set ---------------------------------
    def action_stop_logging(self):
        self.log_stop.set()
    

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
            ,row=1
            ,columnspan=3
            ,sticky=tk.EW
        )


#------------------------ Start GUI ---------------------------------
main=IO_MAIN()
main.win.mainloop()