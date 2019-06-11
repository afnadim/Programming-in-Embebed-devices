#Author:S M ABDULLAH FERDOUS
#Part of CM2540 final coursework
#this is one of the main file of the program which linked many other module together
import time
import picamera
from picamera import PiCamera
from gpiozero import MotionSensor
from datetime import datetime
from tkinter import *
from email_client import email_client
import email.utils
import picture
import sys
import os
import datetime
from IRSensor import *
import time
from  HomesecurityFSM import *

# turn debugging statements on (True), off (False)
DEBUG = True

# declare GUI class that uses an association
# between GUI instance and root window
class GUI:
     
    # define constructor initialiser method
    def __init__(self):
        # construct HomesecurityFSM
        self.fsm = HomesecurityFSM()
        self.fsm.start()
        
        
        # construct root window
        self.root = Tk()
        self.root.title('Home Security system')
        self.root.geometry('400x300')
        
        # label to display state
        self.label = Label(self.root, relief=RAISED)
        self.label.pack(fill=BOTH, expand=1)
        self._display_state(self.fsm.state)
        self.buttonframe = Frame(self.root)
        
        # divide frame into columns, rows of equal weight
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.buttonframe.rowconfigure(0, weight=1)
        self.buttonframe.rowconfigure(1, weight=1)
        self.buttonframe.rowconfigure(2, weight=1)
        #Assign button click events and and button labels
        button = Button(self.buttonframe, text = 'up', command = (lambda name='up' : self._buttonClickEvent(name)))
        button.grid(row=1, column=1, sticky=N+S+E+W)
        button = Button(self.buttonframe, text = 'left', command = (lambda name='left' : self._buttonClickEvent(name)))
        button.grid(row=2, column=0, sticky=N+S+E+W)
        button = Button(self.buttonframe, text = 'down', command = (lambda name='down' : self._buttonClickEvent(name)))
        button.grid(row=2, column=1, sticky=N+S+E+W)
        button = Button(self.buttonframe, text = 'right', command = (lambda name='right' : self._buttonClickEvent(name)))
        button.grid(row=2, column=2, sticky=N+S+E+W)
        self.buttonframe.pack(fill=BOTH, expand=1)
        
        # bind arrow keys on keyboard and Sense Hat joystick
        self.root.bind('<Left>', self._keyEvent)
        self.root.bind('<Right>', self._keyEvent)
        self.root.bind('<Up>', self._keyEvent)
        self.root.bind('<Down>', self._keyEvent)
        self.root.focus_force()
        
        # construct IRsensor object and register callback
        self.IRsensor = IRSensor(self._IRSensorEvent)
        
    # creating functions for diffrent activities
   
    def start(self):
        self.root.mainloop()

    def _keyEvent(self, event):
        key_name = event.keysym.lower()
        output = self.fsm.step(key_name+'E')
        self._display_state(self.fsm.state)

    def _buttonClickEvent(self, button_name):
        # add 'E' to signal this is an event
        output = self.fsm.step(button_name+'E')
        self._display_state(self.fsm.state)

    def _display_state(self, state_name):
     
        # config state label
        self.label.config(text=state_name)
        #GUI levels for diffrent stages and other tasks
        if self.fsm.state=='deactivatedS':
            Monitor.monitor_inactive_redcross()
            self.label.config(text=('Dactivated'))
            
        if self.fsm.state=='deactivatedUpS':
            self.label.config(text=('Deactivated:Waiting for user input'))
            
        if self.fsm.state=='deactivatedDownS':
            self.label.config(text=('Deactivated:Waiting for user input'))
            
        if self.fsm.state=='deactivatedLeftS':
            self.label.config(text=('Dactivated:Waiting for user input'))
            
  
        if self.fsm.state=='dactivatedRightS':
            self.label.config(text=('Deactivated:monitor will be active in 60 seconds'))
        #60 seconds or 60000 milliseconds wait once the sequence is accepted
            self.root.after(60000)
            
        if self.fsm.state=='activatedS':
            self.label.config(text=('Activated'))
            
        if self.fsm.state=='activatedUpS':
            self.label.config(text=('Activated'))
            
        if self.fsm.state=='activatedDownS':
            self.label.config(text=('Activated'))
            
        if self.fsm.state=='activatedLeftS':
            self.label.config(text=('Activated'))
            
        if self.fsm.state=='activatedRightS':
            self.label.config(text=('Dactivated'))
            
    # creating IRsensor event and giving it task  once the motion is detected

    def _IRSensorEvent(self, channel):
        output = self.fsm.step('IRSensorE')
        self._display_state(self.fsm.state)
        if self.fsm.state=='activatedS':
            output = self.fsm.step('IRSensorE')
            self._display_state(self.fsm.state)
            print("Motion detected!")
            #saveing the pictures in a specific folder
            os.chdir('/home/pi/Desktop/Home_security/static')
            #takeing the picture by calling take_picture method from picture
            img=picture.take_picture()
            #directory for email credentials
            os.chdir('/home/pi/Desktop/Home_security')
            #creating email_client object
            email_user=email_client()
            #message and the time of the event
            body=('intruder detected at {}'.format(datetime.datetime.now()))
            email_user.send_email('intruder detected', body)              
 
#testing the method
if __name__ == '__main__':
    app = GUI()
    app.start()

        
