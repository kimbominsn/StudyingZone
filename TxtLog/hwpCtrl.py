import win32com.client as win32
import win32gui
import win32con
import pythoncom

class HWP():

    def __init__(self):
        pythoncom.CoInitialize()
        self.hwp = win32.gencache.EnsureDispatch('HWPFrame.HwpObject')
        self.hwp.RegisterModule("FilePathCheckDLL","SecurityModule")
        # self.Open(fName,"HWP","forceopen:true")

    def quit(self):
        self.hwp.Quit()


    # hwnd = win32gui.FindWindow(None, "빈 문서 1 - 한글")
    # self.hwp.Run("FileNew")
    # hwnd=win32gui.FindWindow(None, "qlsdkfjalkdf")
    # hwnd

    def write(self,s):
        act=self.hwp.CreateAction("InsertText")
        set=act.CreateSet()
        act.GetDefault(set)
        set.SetItem("Text",s)
        act.Execute(set)
        

    def read(self, fName):
        self.hwp.Open(fName, "HWP", "forceopen:true")
        self.hwp.InitScan()

        rst=list()
        while True:
            
            result=self.hwp.GetText()
            # print('result: ', result)
            rst.append(result[1])
            if result[0] == 1:
                break
            elif result[0]==0:
                rst.append('No valid Data')
                break
            elif result[0]==101:
                rst.append('HWP module is not initialized : Run InitScan() first')
                break
            elif result[0]==102:
                rst.append('Text convert failed')
                break

        self.hwp.ReleaseScan()
        self.quit()
        return rst

    def savaAs(self, fName):
        self.hwp.SaveAs(fName)
        self.quit()

    
# hwp=HWP()

# hwp.write("success")
# hwp.savaAs("C:/TestDir/test2.hwp")

# hwp=HWP()

# lines=hwp.read("C:\TestDir\test2.hwp")

