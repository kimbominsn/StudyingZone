import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog as fd
from PyQt5.QtGui import QStandardItemModel, QStandardItem   #QListView에 추가할 model용 library
from GUI_PyQt5_logging import Ui_MainWindow
from FileOpen import Logging    #FileOpen.py
from queue import Queue

import threading
from threading import Thread


fileTypes=['txt','hwp','xlsx', 'docx']
class TxtLogging():
    def __init__(self):
        app=QtWidgets.QApplication(sys.argv)
        self.MainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.update_widgets()
        self.set_default_var()
        self.initialize_queue()
        self.widget_actions()
        self.MainWindow.show()
        sys.exit(app.exec_())

    #widgets callback function
    def widget_actions(self):
        self.ui.actionExit.setStatusTip('Click to exit the application')
        self.ui.actionExit.triggered.connect(self.close_GUI)
        self.ui.btn_browse.clicked.connect(self.action_openfilebrowse) # type: ignore
        self.ui.btn_start.clicked.connect(self.action_startlogging) # type: ignore
        self.ui.btn_stop.clicked.connect(self.action_stoplogging) # type: ignore
        self.ui.btn_load.clicked.connect(self.action_loadFolder) # type: ignore
        self.ui.cb_filetype.activated[str].connect(self.event_cb_fType)
        self.ui.lv_folder.clicked.connect(self.action_list_selected)

    def update_widgets(self):
        # self.MainWindow.setWindowTitle('')
        self.set_default_fDir()

    def set_default_fDir(self):
        self.fDir="C:/TestDir"
        self.ui.txt_fDir.setText(self.fDir)

    def set_default_var(self):
        self.FileTypesIdx=0                 #default Idx : txt
        self.log_stop=threading.Event()
        self.lmodel=QStandardItemModel()
        # self.radVar=tk.IntVar()
        # self.list_cnt=tk.StringVar()  

    def initialize_queue(self):
        self.src_queue=Queue()                  #queue for gui log
        self.logFile=Logging(self.src_queue, self.fDir, fileTypes[self.FileTypesIdx])

        


    def event_cb_fType(self, text):
        # print(text)
        for idx in range(len(fileTypes)):
            if fileTypes[idx]==text:
                self.FileTypesIdx=idx
                break

        self.logFile.log_ftype(fileTypes[self.FileTypesIdx])
                
    def print_queue_messages(self, log_stop):
        while True:
            #Make sure 'QTextCursor' is registered using qRegisterMetaType() 어떻게 해결하지?
            self.ui.txt_log.append(self.src_queue.get())
            if not log_stop:
                break

    def close_GUI(self):
        self.MainWindow.close()

    def action_openfilebrowse(self):
        # pass
        self.fDir=fd.getExistingDirectory(self.MainWindow, "Select folder directory to restore log files... ","")
        self.ui.txt_fDir.clear()
        self.ui.txt_fDir.setText(self.fDir)

    def action_startlogging(self):
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

    def action_stoplogging(self):
        self.log_stop.set()

    def action_loadFolder(self):
        file_list=os.listdir(self.fDir)
        
        self.ui.lb_count.setText("count:"+str(len(file_list)))
        # self.ui.lv_folder.
        for lst in file_list:
            self.lmodel.appendRow(QStandardItem(lst))
        
        self.ui.lv_folder.setModel(self.lmodel)

    def action_list_selected(self):

        data_idx=self.ui.lv_folder.selectedIndexes()
        lines=self.logFile.log_read(self.lmodel.data(data_idx[0]))
        
        self.ui.txt_fileoutput.clear()  #이전 결과값 삭제
        
        if lines:
            for line in lines:
                self.ui.txt_fileoutput.insertPlainText(line)
        else:
            self.ui.txt_fileoutput.setText('not supported file type')

if __name__=="__main__":
    TxtLogging()