#Author:S M Abdullah Ferdous as a Part of CM2540 final coursework
import os
import signal
import subprocess
from tkinter import *
import time

class admin_GUI:
    def __init__(self):
        # constructing the root window
        self.root = Tk()
        self.root.title('System Admistration for Monitoring ')
        self.root.geometry('500x400')

        self.buttonframe = Frame(self.root)
        self.label = Label(self.root, relief=RAISED)
        self.label.pack(fill=BOTH, expand=1)
        self.buttonframe = Frame(self.root)
        # divideing frame into columns, rows of equal weight
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.buttonframe.rowconfigure(0, weight=1)
        self.buttonframe.rowconfigure(1, weight=1)
        self.buttonframe.rowconfigure(2, weight=1)

        self.monitor_pid = None
        self.flask_pid = None
        button = Button(self.buttonframe, text = 'Start Monitoring', command =self.start_monitor)
        button.grid(row=1, column=0, sticky=N+S+E+W)
        button = Button(self.buttonframe, text = 'Start flask Server', command =self.start_flask)
        button.grid(row=2, column=0, sticky=N+S+E+W)
        button = Button(self.buttonframe, text = 'stop monitoring', command =self.kill_monitor)
        button.grid(row=1, column=1, sticky=N+S+E+W)
        button = Button(self.buttonframe, text = 'Stop flask Server', command =self.kill_flask)
        button.grid(row=2, column=1, sticky=N+S+E+W)
        button = Button(self.buttonframe, text = 'Delete all images from flask Server', command =self.delet_image)
        button.grid(row=2, column=2, sticky=N+S+E+W)

        self.buttonframe.pack(fill=BOTH, expand=1)
    #call the process to start monitoring    
    def start_monitor(self):
        cmd = ['sudo','python3','Main_Gui.py']
        pro = subprocess.Popen(cmd,  preexec_fn=os.setsid)
        #print(pro.pid)
        self.monitor_pid = pro.pid
    #to stop monitoring
    def kill_monitor(self):
        os.killpg(self.monitor_pid, signal.SIGTERM)
    #starting the flask server
    def start_flask(self):
        cmd = ['sudo','python3','Flask_server.py']
        proc = subprocess.Popen(cmd,  preexec_fn=os.setsid)
        self.flask_pid=proc.pid
    #stopping the flask server
    def kill_flask(self):
        os.killpg( self.flask_pid, signal.SIGTERM)
    #delet all the files from the directory for flask images
    def delet_image(self):
        files=os.listdir('/home/pi/Desktop/Home_security/static')
        for f in files:
            if f.endswith(".jpg"):
                os.remove('/home/pi/Desktop/Home_security/static/' + f)
        
#unit test
if __name__ == '__main__':
    app = admin_GUI()

