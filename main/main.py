### main.py


import time
import RPi.GPIO as GPIO

import irDoor
import StepperMotor

## set mode of GPIO
GPIO.setmode(GPIO.BCM)

## Pins set up

## stepper motor 1 - Door
motor1_in1 = 17
motor1_in2 = 18
motor1_in3 = 27
motor1_in4 = 22

## stepper motor 2 - Classifier
## in1 = 23
# in2 = 24
# in3 = 25
# in4 = 10
motor2_in1 = 23
motor2_in2 = 24
motor2_in3 = 25
motor2_in4 = 10

def classify(object_type):
    ## classify object depending on the result

    if object_type == 1:
        direction = False
        steps = 4096
        motor = StepperMotor.StepperMotor(motor2_in1, motor2_in2, motor2_in3, motor2_in4, direction)
        motor.activate()
        motor.reverse_direction()

    if object_type == 2:
        direction = True
        steps = 4096
        motor = StepperMotor.StepperMotor(motor2_in1, motor2_in2, motor2_in3, motor2_in4, direction)
        motor.activate()
        motor.reverse_direction()


def startCamera():
    ## run detection for 15 seconds
    ## get last detection result or most accurate (highest percentage)
    return detection_result


def openDoor():
    ## activate the door to open
    door_motor = StepperMotor.StepperMotor(motor1_in1, motor1_in1, motor1_in, motor1_in1)
    door_motor.activate()
    door_motor.reverse_direction()
    return True
    ## stepper motor
    ## close the door
    ## start reading from camera


def checkDoor():
    ir_door_pin = 40
    GPIO.setup(ir_door_pin, GPIO.IN)
    try:
        while True:
            # initiated an infinite while loop
            if not GPIO.input(ir_door_pin):
                ## if there is something near detected
                ## start reading from camera
                while not GPIO.input(ir_door_pin):
                    # checking input on sensor again
                    time.sleep(0.2)
                    # generate time delay of 0.2 seconds
            else:
                return True
    except:
        GPIO.cleanup()


def main():
    ## Read from IR_Door
    if checkDoor():
        if openDoor():
            if startCamera():
                result = startCamera()
                classify(result)
        else:
            print("ERROR: open door")
    else:
        print("ERROR: reading from door")


if __name__ == '__main__':
    main()
