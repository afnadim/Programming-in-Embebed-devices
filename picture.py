#Author:S M Abdullah Ferdous as a Part of CM2540 final coursework
import time
import picamera
import Monitor
import IRSensor
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('Error importing RPi.GPIO!\n',
          'This is probably because you need superuser privileges.\n',
          'You can achieve this by using "sudo" to run your script')
#creating the file name with date,time
def getFileName():
        filename = time.strftime("%Y%m%d-%H%M%S.jpg")
        return filename
#declareing the camera
camera=picamera.PiCamera()
#fliping the picture 
camera.vflip=True
#function to take the picture
def take_picture():
        Filename= getFileName()
        camera.capture(Filename)
        print("Picture Taken")



