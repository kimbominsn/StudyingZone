import pandas as pd
import os
from GUI_File_encoding import Ui_MainWindow
import sys
from AESCipher import Cipher
from user_db import user_db
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog as fd
import xlsxwriter
from user_db_mysql import MySQL
import binascii

# os.makedirs(self.dst_dir, exist_ok=True)
# df=pd.read_excel(fileToRead)

class File_Main():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self.MainWindow)
        self.update_widgets()
        self.widget_actions()
        self.MainWindow.show()
        sys.exit(app.exec_())


    def update_widgets(self):
        self.MainWindow.setWindowTitle('Excel file encoding')
        self.set_default_fdir()
        self.mySQL=MySQL()
        self.load_mysql_users()
        
    
    def load_mysql_users(self):
        self.users=self.mySQL.showUsers()
        idx=0
        for us in self.users:
            print(us)
            self.ui.txt_getID.insertItem(idx, str(us[0]))
            idx+=1

        
    def widget_actions(self):
        self.ui.btn_file.clicked.connect(self.action_filebrowse)
        self.ui.btn_encoding.clicked.connect(self.action_encoding)
        self.ui.btn_createUser.clicked.connect(self.action_createUser)
        self.ui.txt_getID.activated[int].connect(self.event_cb_getSalt)

    def event_cb_getSalt(self, idx):
        self.users=self.mySQL.showUsers()
        self.userID=self.users[idx][0]
        self.password=self.users[idx][1]
        self.password=self.password.encode('utf-8')
        self.ui.txt_getSalt.setText(self.password.decode())
  
    def set_default_fdir(self):
        self.fName='C:/encodingTest/test1.xlsx'
        self.ui.txt_file.setText(self.fName)
        self.password=''
        # self.userID=''

    def action_filebrowse(self):
        self.fName=fd.getOpenFileName(self.MainWindow, "Select folder directory to restore log files... ")[0]
        self.ui.txt_file.clear()
        self.ui.txt_file.setText(self.fName)

    def action_createUser(self):
        self.user=user_db() #암호화 키 생성 클래스
        
        self.password=self.user.salt
        self.ui.txt_getSalt.setText(self.password.decode())
        listP=(self.password.decode(),)
        self.userID=self.mySQL.insertUsers(listP)   #USER ID / salt 값 Mysql에 업데이트 후 last point idx(user_id) 받음
        # self.load_mysql_users()
        # print(len(self.ui.txt_getID))
        
        self.ui.txt_getID.insertItem(len(self.ui.txt_getID), str(self.userID))
        self.MainWindow.show()
        # self.mySQL.showUsers()

    def action_encoding(self):
        if not self.password:
            self.MainWindow.statusBar().showMessage('Please Create UserData First')
            return

        aes=Cipher(self.password)
        aes.encrypt_file(self.fName, out_filename='C:/encodingTest/UserID_'+str(self.userID)+'_'+self.fName.split('/')[-1]+'.enc')
        # os.remove(self.fName)


    def read_excel_file(self, fName):
        df=pd.read_excel(fName)
        print(df.columns[0])

        return df.columns[0]




if __name__ == "__main__":
    File_Main()