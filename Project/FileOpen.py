from datetime import datetime
import random
import os
from time import sleep

class Logging():

    def __init__(self, log_queue):
        self.RESULT=['OK', 'NG']
        self.path="c:\TestDir"
        self.make_directory()
        log_queue.put(' Log Directory :'+ self.path+'\n')

    def make_directory(self):
        os.makedirs(self.path, exist_ok=True)


    def start_logging(self, log_queue, stop_event):
        while True:
            strResult=random.choice(self.RESULT)
            date_now=datetime.now().strftime('%Y%m%d %H%M%S')
            self.LogFile=f"{self.path}\{date_now} {strResult}.txt"
            try:
                file=open(self.LogFile, 'a+', encoding="utf-8")

                file.write(strResult)
                file.close()
                log_queue.put(self.LogFile+' written.\n')
                sleep(1)
            except FileNotFoundError:
                log_queue.put('Directory is not found.\n')
                self.make_directory()
                log_queue.put('Creating Directory.... Start again..\n')
                break

            except Exception as e:
                print(e)
                log_queue.put(e)
                break
            
            if stop_event.is_set():
                log_queue.put('Logging stopped.\n')
                break
            



   

    
    


    

    


    

