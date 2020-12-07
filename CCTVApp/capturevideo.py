import cv2 as cv 
from datetime import datetime


class CaptureVideo():
    def __init__(self):
        self.cap=cv.VideoCapture(0)
        fourcc=cv.VideoWriter_fourcc(*'XVID')
        #Date and time The video was taken.
        now=datetime.now()
        videoname=now.strftime("%m-%d-%y,%H:%M:%S")
        videoName='CCTV Video:'+videoname+'.avi'
        self.width=6480
        self.height=480
        self.out=cv.VideoWriter(videoName,fourcc,5.0,(640,480))
        print(self.cap.isOpened())
        #Time Display text properties.
        self.font=cv.FONT_HERSHEY_SIMPLEX
        self.org=(20,20)
        self.fontscale=0.6
        self.color=(100,0,125)
        #Setting font thickness.
        self.thickness=1
    def video(self):
        while(open):
                self.ret,self.frame=self.cap.read()
                if self.ret==True:
                    self.Today=datetime.now()
                    self.Day=self.Today.strftime("%m-%d-%y,%H:%M:%S")
                    self.frame=cv.putText(self.frame,self.Day,self.org,self.font,self.fontscale,self.color,self.thickness,cv.LINE_AA)
                    self.out.write(self.frame)
                    cv.imshow("Video:",self.frame)
                else:
                    break
                key=cv.waitKey(1)
                if key==ord('q'):
                    break
                 




        self.cap.release()
        self.out.release()
        cv.destroyAllWindows()


if __name__=="__main__":
    capture=CaptureVideo()
    capture.video()

