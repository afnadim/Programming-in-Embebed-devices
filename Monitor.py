#Author:S M Abdullah Ferdous as a Part of CM2540 final coursework
#to create LED displays for diffrent stages and action

from sense_hat import SenseHat
from random import randint
from time import sleep
import time

#from tkinter import*
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *

#import senseHat as sense
sense=SenseHat()
d=(255,0,0)#red
w=(200,200,200)#white
t=(124,252,0)#green
e=(0,0,0)#empthy

#function for first stage of the monitor
#red cross first stage

##--------------------------------------------------------------------
def monitor_inactive_redcross():
    
    #monitor output
    monitor_status=[
    d,e,e,e,e,e,e,d,
    e,d,e,e,e,e,d,e,
    e,e,d,e,e,d,e,e,
    e,e,e,d,d,e,e,e,
    e,e,e,d,d,e,e,e,
    e,e,d,e,e,d,e,e,
    e,d,e,e,e,e,d,e,
    d,e,e,e,e,e,e,d
    ]
        
    
    return sense.set_pixels(monitor_status)

##--------------------------------------------------------------------  

#function for the second stage 
#red right arrow second stage
def monitor_red_arrow():

    
    
    monitor_status=[
    e,e,e,d,d,d,e,e,
    e,e,e,e,d,d,d,e,
    e,e,e,e,e,d,d,d,
    d,d,d,d,d,d,d,d,
    d,d,d,d,d,d,d,d,
    e,e,e,e,e,d,d,d,
    e,e,e,e,d,d,d,e,
    e,e,e,d,d,d,e,e

    ]
     
    return sense.set_pixels(monitor_status)
    
##--------------------------------------------------------------------
#red circle
def monitor_red_circle():
    
    monitor_status=[
    e,e,e,d,d,d,e,e,
    e,e,d,e,e,e,d,e,
    e,d,e,e,e,e,e,d,
    e,d,e,e,e,e,e,d,
    e,d,e,e,e,e,e,d,
    e,e,d,e,e,e,d,e,
    e,e,e,d,d,d,e,e,
    e,e,e,e,e,e,e,e

    ]
   
    return sense.set_pixels(monitor_status)

##--------------------------------------------------------------------
#Green circle
def monitor_green_circle():

    
    monitor_status=[
    e,e,t,t,t,t,e,e,
    e,t,t,t,t,t,t,e,
    t,t,t,t,t,t,t,t,
    t,t,t,t,t,t,t,t,
    t,t,t,t,t,t,t,t,
    e,t,t,t,t,t,t,e,
    e,e,t,t,t,t,e,e,
    e,e,e,e,e,e,e,e

    ]
    
    
    return sense.set_pixels(monitor_status)

##--------------------------------------------------------------------

#left green arrow.activated after password
def monitor_green_arrow():
     
    monitor_status=[
    e,e,e,e,t,e,e,e,
    e,e,e,t,e,e,e,e,
    e,e,t,e,e,e,e,e,
    e,t,t,t,t,t,t,t,
    e,t,t,t,t,t,t,t,
    e,e,t,e,e,e,e,e,
    e,e,e,t,e,e,e,e,
    e,e,e,e,t,e,e,e

    ]
    
    return sense.set_pixels(monitor_status)


#unit test by calling al the fucntions separately
'''
monitor_inactive_redcross()
monitor_red_arrow()
monitor_red_circle()
monitor_green_circle()
monitor_green_arrow()



'''
