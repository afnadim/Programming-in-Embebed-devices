#Author:S M Abdullah Ferdous as a Part of CM2540 final coursework

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('Error importing RPi.GPIO!\n',
          'This is probably because you need superuser privileges.\n',
          'You can achieve this by using "sudo" to run your script')

class IRSensor:
    # pin definitions as class constants
    IRSENSOR = 40 # pyro input channel 
    
    def __init__(self, callback):

        # use P1 header pin numbering convention
        GPIO.setmode(GPIO.BOARD)

        # configure pin 40 as input
        GPIO.setup(IRSensor.IRSENSOR, GPIO.IN)
        # setup IR event handling
  
        GPIO.add_event_detect(IRSensor.IRSENSOR, GPIO.RISING, callback=callback)














        
'''
class IRSensor:
    GPIO.setmode(GPIO.BOARD)
        ##camera declration
    camera = PiCamera()
        #declareing motion sensor


        # configure pin 40 as input
    GPIO.setup(40, GPIO.IN)

        # define callback function to be called in event of
        #creating file name
    def getFileName():
        filename = time.strftime("%Y%m%d-%H%M%S.gif")
        return filename


    def IRevent(channel):
        print("IR event on channel {0} detected".format(channel))

    # setup IR event handling
    GPIO.add_event_detect(40, GPIO.RISING, callback=IRevent)
    while True:
        camera.capture(getFileName())
    '''
