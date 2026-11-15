import RPi.GPIO as GPIO

#importing the library of RPi.GPIO

import time

#importing the library of time

sensor = 21

#declaring BCM pin 18 which is GPIO 24 of Raspberry Pi

## to use board pin numbers instead : GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
#declaring the BCM mode of pins

GPIO.setup(sensor,GPIO.IN)

#set the behaviour of sensor as input

def loop():
    try:
        while True:
        #initiated a infinite while loop
            if GPIO.input(sensor):
                ## if there is none
                

                print("False")

                #led turned on

                while GPIO.input(sensor):

                    #checking input on sensor again

                    time.sleep(0.2)

                    #generate time delay of 0.2 seconds

            else:
                print("True")
                sendMessage()
                break
                time.sleep(0.5)

            #led turned off if there is no input on sensor

    except KeyboardInterrupt:

    #if any key is pressed on keyboard terminate the program

        GPIO.cleanup()

        #cleanup the GPIO pins for any other program use
    
def sendMessage():
    print("Hi, we received a true message")
    time.sleep(1)
    loop()
    
if __name__ == "__main__":
    loop()