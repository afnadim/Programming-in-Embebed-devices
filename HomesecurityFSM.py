# Author:S M Abdullah Ferdous as a Part of CM2540 final coursework
# subclass inheriting from FSM
# implements actual Home_security system FSM

from FSM import *
import Monitor
import time


class HomesecurityFSM(FSM):
    # define start state for FSM
    startState = 'deactivatedS'
    # method that determines the next state transition
    # input parameters: (current) state, input (if any)
    # returns: (next) state, output
    # N.B. the method does not actually implement
    # the next state transition that is left up to
    # inherited method FSM.step()
    def getNextValues(self, state, inp):
        if state == 'deactivatedS':
            if inp == 'deactivatedS':
                return ('deactivatedS', Monitor.monitor_inactive_redcross())   
            elif inp == 'upE':
                return ('deactivatedUpS', Monitor.monitor_red_arrow())    
            else:
                return ('deactivatedS', Monitor.monitor_inactive_redcross())

        elif state == 'deactivatedUpS':
            if inp == 'downE':
                return ('deactivatedDownS', Monitor.monitor_red_arrow())
            else:
                return ('deactivatedS', Monitor.monitor_inactive_redcross())

        elif state == 'deactivatedDownS':
            if inp == 'leftE':
                return ('deactivatedLeftS', Monitor.monitor_red_arrow())
            else:
                return ('deactivatedS', Monitor.monitor_inactive_redcross())
        elif state == 'deactivatedLeftS':
            if inp == 'rightE':
                return ('dactivatedRightS', Monitor.monitor_red_circle()) 
            else:
                return ('deactivatedS', Monitor.monitor_inactive_redcross())

        elif state == 'dactivatedRightS':
            if inp == 'IRSensorE':
                return ('activatedS', Monitor.monitor_green_circle())
            else:
                return ('activatedS',Monitor.monitor_green_circle())
        
        #--------------------------------------------------------
      #Deactivateing the code with right sequence
    
        elif state == 'activatedS':
            if inp == 'upE':
                return ('activatedUpS',Monitor.monitor_green_arrow())
            else:
                return ('activatedS',Monitor.monitor_green_circle())
        elif state == 'activatedUpS':
            if inp == 'downE':
                return ('activatedDownS',Monitor.monitor_green_arrow())
            else:
                return ('activatedS', Monitor.monitor_green_circle())
        elif state == 'activatedDownS':
            if inp == 'leftE':
                return ('activatedLeftS',Monitor.monitor_green_arrow())
            else:
                return ('activatedS', Monitor.monitor_green_circle())
        elif state == 'activatedLeftS':
            if inp == 'rightE':
                return ('deactivatedS',Monitor.monitor_inactive_redcross())
            else:
                return ('activatedS',Monitor.monitor_green_circle())
       
  
# unit test
if __name__ == '__main__':
    # define list of inputs to test the FSM
    testInputs = ['upE', 'downE', 'leftE', 'rightE', 'IRSensorE'\
                  'upE', 'downE', 'leftE', 'rightE']
    # construct and initialise FSM
    ts = HomesecurityFSM()
    ts.start()
    # display start state
    print('Start state:', ts.state)
    # display all state transitions prompted by
    # the specified list of test inputs
    for total_state in ts.transduce(testInputs):
        # display input, output, next state
        print(('In: {0[0]:<20s} '+
              'Out: {0[1]:<10s} '+
              'Next state: {0[2]:<10s}')
              .format(total_state))
               

    
