from datetime import datetime
import random
import os
from time import sleep
from docx import Document
 #pip install python-docx
# import win32com.client as win32
#  #pip install pypiwin32
# import olefile
import pandas as pd
class Logging():

    def __init__(self, log_queue):
        self.RESULT=['OK', 'NG']
        self.dst_dir="c:\TestDir"
        self.make_directory()
        log_queue.put(' Log Directory :'+ self.dst_dir+'\n')

    # directory가 없는 경우 생성
    def make_directory(self):
        os.makedirs(self.dst_dir, exist_ok=True)

    def log_init(self, fileType):
        self.strResult=random.choice(self.RESULT)
        self.date_now=datetime.now().strftime('%Y%m%d %H%M%S')
        self.LogFile=f"{self.dst_dir}/{self.date_now} {self.strResult}.{fileType}"
        

    def log_write(self, fileType):
        if fileType=='txt':
            file=open(self.LogFile, 'a+', encoding="utf-8")
            file.write(self.strResult)
            file.close()
            return True
        elif fileType=='hwp':
            # self.LogFile="C:/TestDir/test2.hwp"
            file=open(self.LogFile, 'a+', encoding="utf-16")
            file.write(self.strResult)
            file.close()
           
            # f=olefile.OleFileIO(self.LogFile)
            # encode_text=f.openstream('PrvText').read()
            # decode_text=encode_text.decode('UTF-16')
            # print(decode_text)
            return True
        elif fileType=='xlsx':
            # self.LogFile="C:/TestDir/test2.xlsx"
            df=pd.DataFrame([self.strResult])
            df.to_excel(self.LogFile, index=False, header=False)

            return True
        elif fileType=='docx':
            document=Document()
            document.add_paragraph(self.strResult)
            document.save(self.LogFile)
            return True
        
        

    # directory내 파일 생성 및 log queue에 메시지 put
    def start_logging(self, log_queue, stop_event, fileType):   #fileType : 'txt','hwp','xlsx'
        log_queue.put('Logging started in '+fileType+'\n')
        while True:
            try:
                self.log_init(fileType)
                if self.log_write(fileType):
                    log_queue.put(self.LogFile+' written.\n')
                else:
                    log_queue.put('log write failed.\n')
                    break
                
                sleep(1)
            # directory 소실로 인한 exception 처리
            except FileNotFoundError as err:
                log_queue.put(err)
                self.make_directory()
                log_queue.put('Creating Directory.... Start again..\n')
                break

            except Exception as e:
                print(e)
                log_queue.put(e)
                break
            
            #thead stop flag is set -> stop logging
            if stop_event.is_set():
                log_queue.put('Logging stopped.\n')
                break
            



   

    
    


    

    


    

