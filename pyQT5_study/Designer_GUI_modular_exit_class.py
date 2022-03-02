import sys
from PyQt5 import QtWidgets
from Designer_First_ui_btn_label import Ui_MainWindow

class ExitDesignerGUI():
    def __init__(self):
        app=QtWidgets.QApplication(sys.argv)
        self.MainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.update_widgets()
        self.widget_actions()
        self.MainWindow.show()
        sys.exit(app.exec_())

    def update_widgets(self):
        self.MainWindow.setWindowTitle('hahahah')
        
    def widget_actions(self):
        self.ui.actionExit.setStatusTip('Click to exit the application')
        self.ui.actionExit.triggered.connect(self.close_GUI)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    def close_GUI(self):
        self.MainWindow.close()

if __name__=="__main__":
    ExitDesignerGUI()