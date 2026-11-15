import RPi.GPIO as GPIO
import time


class StepperMotor:
    def __init__(self, in1, in2, in3, in4, direction):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.step_count = 4096  ## 4096 = 360 degrees
        self.direction = direction
        self.step_sleep = 0.0015  ## controls speed of stepper motor
        self.step_sequence = [[1, 0, 0, 1],
                              [1, 0, 0, 0],
                              [1, 1, 0, 0],
                              [0, 1, 0, 0],
                              [0, 1, 1, 0],
                              [0, 0, 1, 0],
                              [0, 0, 1, 1],
                              [0, 0, 0, 1]]

        self.motor_pins = [self.in1,
                           self.in2,
                           self.in3,
                           self.in4]

        self.motor_step_counter = 0

    def setup(self):
        # setting up
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)

        # initializing
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)

    def activate(self):
        self.setup()
        ## i = 0
        for i in range(self.step_count):
            for pin in range(0, len(self.motor_pins)):
                GPIO.output(self.motor_pins[pin], self.step_sequence[self.motor_step_counter][pin])
            if self.direction:
                self.motor_step_counter = (self.motor_step_counter - 1) % 8
            elif not self.direction:
                self.motor_step_counter = (self.motor_step_counter + 1) % 8
            else:  # defensive programming
                print("uh oh... direction should *always* be either True or False")
                self.cleanup()
                exit(1)
            time.sleep(self.step_sleep)
        self.cleanup()

    def reverse_direction(self):
        self.direction = not self.direction
        self.activate()

    def cleanup(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
