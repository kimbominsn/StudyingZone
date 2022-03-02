from GUI_Calculator_modi import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

class CaculatorMain():
    def __init__(self):
        self.clear_variables()
        app=QtWidgets.QApplication(sys.argv)
        self.MainWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.update_widgets()
        self.widget_actions()
        self.MainWindow.show()
        sys.exit(app.exec_())

    def update_widgets(self):
        self.MainWindow.setWindowTitle('Caculator')
        
    def widget_actions(self):
        # pass
        self.ui.btn_0.clicked.connect(lambda:self.action_number_clicked('0'))
        self.ui.btn_1.clicked.connect(lambda:self.action_number_clicked('1'))
        self.ui.btn_2.clicked.connect(lambda:self.action_number_clicked('2'))
        self.ui.btn_3.clicked.connect(lambda:self.action_number_clicked('3'))
        self.ui.btn_4.clicked.connect(lambda:self.action_number_clicked('4'))
        self.ui.btn_5.clicked.connect(lambda:self.action_number_clicked('5'))
        self.ui.btn_6.clicked.connect(lambda:self.action_number_clicked('6'))
        self.ui.btn_7.clicked.connect(lambda:self.action_number_clicked('7'))
        self.ui.btn_8.clicked.connect(lambda:self.action_number_clicked('8'))
        self.ui.btn_9.clicked.connect(lambda:self.action_number_clicked('9'))
        self.ui.btn_dot.clicked.connect(lambda:self.action_number_clicked('.'))

        self.ui.btn_divide.clicked.connect(lambda:self.action_math_clicked('/'))
        self.ui.btn_multiply.clicked.connect(lambda:self.action_math_clicked('*'))
        self.ui.btn_minus.clicked.connect(lambda:self.action_math_clicked('-'))
        self.ui.btn_plus.clicked.connect(lambda:self.action_math_clicked('+'))
        self.ui.btn_clear.clicked.connect(lambda:self.action_clear())
        
        # self.ui.btn_delete.clicked.connect(lambda:self.ui.txt_result.)
        self.ui.btn_is.clicked.connect(self.action_calculation)

    #연산에 쓰이는 변수들
    def clear_variables(self):
        self.num=''
        self.ui_text=''
        self.math=list()
        self.numList=list()
        self.done=False     #

    def action_clear(self):
        self.ui.txt_result.clear()
        self.clear_variables()


    def action_number_clicked(self, strNum):
        # if len(self.math)==0:
        if self.done:
            self.num=''
            self.clear_variables()
        self.num=f"{self.num}{strNum}"  #string으로 숫자값 축적..
        self.ui_text=f"{self.ui_text}{strNum}"
        self.ui.txt_result.setText(self.ui_text) 
        # print(self.num)

    def action_math_clicked(self, strMath):
        if self.done:
            self.done=False
            self.ui_text=self.numList[0]
        else:
            self.numList.append(float(self.num))    #계산할 숫자셋 list에 저장

        self.ui_text=f"{self.ui_text}{strMath}"
        self.ui.txt_result.setText(self.ui_text)    
        self.num=''     #저장한 숫자셋 클리어            
        self.math.append(strMath)   #operator list에 추가
        

        # print(strMath)

    def action_calculation(self):
        self.numList.append(float(self.num))
        self.num=''
        result=self.numList[0]
        idx=1
 
        for oper in self.math:

            if oper=='*':
                result=result*self.numList[idx]
            elif oper=='/':
                result=result/self.numList[idx]
            elif oper=='-':
                result=result-self.numList[idx]
            elif oper=='+':
                result=result+self.numList[idx]
            idx=idx+1

        print(self.ui_text)
        print(f"result={result}")
        self.ui.txt_result.setText(str(result))
        self.clear_variables()

        self.numList.append(result)
        self.done=True
        
    


if __name__=="__main__":
    CaculatorMain()