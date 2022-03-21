from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog as fd
from PyQt5.QtGui import QStandardItemModel, QStandardItem   #QListView에 추가할 model용 library
from GUI_Decoding import Ui_MainWindow
import sys, os

import pandas as pd
from user_db_mysql import MySQL
from AESCipher import Cipher
from qt_material import apply_stylesheet

class FileDecode():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.update_widgets()
        apply_stylesheet(app, theme='light_cyan.xml')
        self.widget_actions()
        self.set_default_fdir()
        self.mySQL=MySQL()
        self.MainWindow.show()
        sys.exit(app.exec_())

    def update_widgets(self):
        self.MainWindow.setWindowTitle('Excel file decoding')
        self.set_default_fdir()
        
        
        
    def widget_actions(self):
        self.ui.btn_File.clicked.connect(self.action_filebrowse)
        self.ui.lv_filelist.clicked.connect(self.action_list_selected)
        self.ui.btn_reload.clicked.connect(self.action_reload)
        

    def set_default_fdir(self):
        self.fDir='C:/encodingTest/'
        self.ui.txt_file.setText(self.fDir)
        self.lmodel=QStandardItemModel()
        self.show_encoded_excel_files()

    def action_filebrowse(self):
        self.fDir=fd.getExistingDirectory(self.MainWindow, "Select folder directory","")
        self.ui.txt_file.clear()
        self.ui.txt_file.setText(self.fDir)
        self.lmodel.clear()
        self.show_encoded_excel_files()

    def action_reload(self):
        self.lmodel.clear()
        self.show_encoded_excel_files()

    def show_encoded_excel_files(self):
        file_list=os.listdir(self.fDir)
        
        for lst in file_list:
            # print(lst)
            if lst.split('.')[-1]=='enc':
                self.lmodel.appendRow(QStandardItem(lst))
        
        self.ui.lv_filelist.setModel(self.lmodel)

    def action_list_selected(self):
        self.ui.txt_result.clear()
        data_idx=self.ui.lv_filelist.selectedIndexes()
        selected_file=self.lmodel.data(data_idx[0])
        userID=(selected_file.split('_')[1],)
        
        salt=self.mySQL.findSalt(userID)
        # print(salt)
        self.AES_decode(salt, selected_file)

    def AES_decode(self, salt, fName):
        
        # line=self.read_excel_file(self.fDir+'/'+fName)
        # aes=Cipher(salt.encode('utf-8'))
        # self.ui.txt_result.insertPlainText('File : '+fName+'\n')
        # self.ui.txt_result.insertPlainText(aes.decrypt(line))

        aes=Cipher(salt.encode('utf-8'))
        
        aes.decrypt_file(in_filename=self.fDir+'/'+fName, out_filename=self.fDir+'/'+fName.split('.')[0]+'.'+fName.split('.')[1])
        self.ui.txt_result.insertPlainText('File : '+fName+'\n')
        self.ui.txt_result.insertPlainText('File decrypted ...\n')
        os.remove(self.fDir+'/'+fName)
        

    def read_excel_file(self, fName):
        df=pd.read_excel(fName)
        print(df.columns[0])

        return df.columns[0]
if __name__ == "__main__":
    FileDecode()
