from GUI_Calculator_additional import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import math

PI=math.pi

class type():
    none='none'
    num='num'
    oper='oper'
    
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

        self.ui.btn_x2.clicked.connect(lambda:self.action_math_clicked('x^2'))
        self.ui.btn_xy.clicked.connect(lambda:self.action_math_clicked('x^y'))
        self.ui.btn_10x.clicked.connect(lambda:self.action_additional_math_clicked('10^x'))
        self.ui.btn_root.clicked.connect(lambda:self.action_additional_math_clicked('root'))
        self.ui.btn_sin.clicked.connect(lambda:self.action_additional_math_clicked('sin'))
        self.ui.btn_cos.clicked.connect(lambda:self.action_additional_math_clicked('cos'))
        self.ui.btn_tan.clicked.connect(lambda:self.action_additional_math_clicked('tan'))
        self.ui.btn_pi.clicked.connect(lambda:self.action_number_clicked('pi'))
        self.ui.btn_delete.setDisabled(True)
        # self.ui.btn_delete.clicked.connect(lambda:self.ui.txt_result.)
        self.ui.btn_is.clicked.connect(self.action_calculation)

    #연산에 쓰이는 변수들
    def clear_variables(self):
        self.num=''
        self.ui_text=''
        self.list_calc=list()
        #{'val':'', 'type':type.num/oper/none, 'prev_type':self.previous_set}
        self.math=list()
        self.numList=list()
        self.done=False     #
        self.previous_set=type.none    #'none'/'num'/'oper'

    def append_ui_text(self, str):
        if str=='x^2':
            str='^2'
        elif str=='x^y':
            str='^'
        elif str=='10^x':
            str='10^'
        self.ui_text=f"{self.ui_text}{str}"
        self.ui.txt_result.setText(self.ui_text)

    def action_clear(self):
        self.ui.txt_result.clear()
        self.clear_variables()


    def action_number_clicked(self, strNum):
        #연산 후 (=) 바로 입력을 받는경우
        if self.done:
            self.num=''
            self.clear_variables()  #숫자의 경우에는 새로운 입력으로 간주.. 이전데이터 모두 삭제
        
        
        if strNum=='pi':
            self.complete_numset()  #연속 입력된 숫자 완료
            if self.previous_set==type.num:
                #파이 입력 시 숫자 뒤 바로 PI를 붙이는 경우 곱셈연산하여 하나의 인자로 처리
                temp=self.list_calc[-1].get('value')*PI
                self.list_calc[-1]['value']=temp
            else:
                self.list_calc.append({'value':PI, 'type':type.num, 'prev_type':self.previous_set})
                self.previous_set=type.num
            
            self.num=''
        else:
            self.num=f"{self.num}{strNum}"  #string으로 숫자값 축적..
        self.append_ui_text(strNum)
        # self.previous_set='Number' 
    
    def validation_check_oper(self,str):
        if self.previous_set==str:
            self.clear_variables()
            self.ui.txt_result.setText('Invalid input. Try again')

            return False
        else:
            return True

    def action_math_clicked(self, strMath):
        #인자가 앞뒤로 붙는 연산자들...
        if self.done:
            self.done=False
            self.ui_text=self.list_calc[0].get('value')
        else:
            self.complete_numset()  #연속 입력된 숫자 완료
        
        if not self.validation_check_oper(type.none):  #연산자 앞 뒤로 인자가 들어와야함.. prev_set이 없는경우 에러
            return
        
        self.append_ui_text(strMath)  
    
        self.list_calc.append({'value':strMath, 'type':type.oper, 'prev_type':self.previous_set})
        self.previous_set=type.oper

    def action_additional_math_clicked(self, strMath):
        #sin, cos, tan, 10^x, root

        if self.done:
            #연산자 뒤에 인자가 붙으므로 새로운 연산 시작
            self.done=False
            self.clear_variables()
        else:
            self.complete_numset()  #연속 입력된 숫자 완료

            if not self.validation_check_oper(type.num):   #연산자 앞에 인자가 붙지 않도록 prev_set이 숫자인 경우 에러
                return

        self.append_ui_text(strMath)

        self.list_calc.append({'value':strMath, 'type':type.oper, 'prev_type':self.previous_set})
        self.previous_set=type.oper
        

    def complete_numset(self):
        if not self.num:
            return
        elif self.num==str(PI):
            return
        else:
            self.list_calc.append({'value':float(self.num), 'type':type.num, 'prev_type':self.previous_set})
            self.previous_set=type.num
            self.num=''

    def action_calculation(self):
        self.complete_numset()  #연속 입력된 숫자 완료

        #임시변수들
        result=0.0
        temp_val=list()
        operator=list()

        if len(self.list_calc)==1 and (self.previous_set==type.num):
            #숫자입력만 1개 들어온 경우 해당 숫자만 결과값으로 반환
            result=self.list_calc[0].get('value')
        else:
            for lst in self.list_calc:
            #입력받은 값들을 type에 따라 분류
                if lst['type']==type.num:
                    temp_val.append(lst.get('value'))
    
                elif lst['type']==type.oper:
                    operator.append(lst.get('value'))

            #분류된 값들을 함수로 넘겨 최종 계산
            try:
                result=self.calculate_values(temp_val,operator)
                temp_val.clear()
                print(self.ui_text)
                print(f"result={result}")
                self.ui.txt_result.setText(str(round(result,6)))    #결과값은 소수점 6자리로 반올림
                self.clear_variables()

                self.list_calc.append({'value':result, 'type':type.num, 'prev_type':self.previous_set})
                self.previous_set=type.num
                self.num=''
                self.done=True
            except Exception as e:
                self.ui.txt_result.setText(str(e))
                self.clear_variables()
            

        

    def calculate_values(self, temp_val, oper):
        #단일계산만 가능... 연속수식은 추후...
        result=0.0

        for op in oper:
            
            if len(temp_val)==self.value_len_check(op):
                if op=='*':
                    result=temp_val[0]*temp_val[1]
                elif op=='/':
                    result=temp_val[0]/temp_val[1]
                elif op=='-':
                    result=temp_val[0]-temp_val[1]
                elif op=='+':
                    result=temp_val[0]+temp_val[1]
                elif op=='x^y':
                    result=temp_val[0]**temp_val[1]

                elif op=='x^2':
                    result=temp_val[0]**2
                
                elif op=='10^x':
                    result=10**temp_val[0]
                elif op=='root':
                    result=math.sqrt(temp_val[0])
                elif op=='sin':
                    result=math.sin(temp_val[0])
                elif op=='cos':
                    result=math.cos(temp_val[0])
                elif op=='tan':
                    result=math.tan(temp_val[0])

        return result


    def value_len_check(self, oper):
        num_val=0
        if oper=='*' or oper=='/' or oper=='-' or oper=='+' or oper=='x^y':
            num_val=2
        else:
            num_val=1
        
        return num_val


if __name__=="__main__":
    CaculatorMain()