
from adafruit_servokit import ServoKit
import threading
import time

kit = ServoKit(channels=16)

class Servo():
    def __init__(self, number, angle, start, end):
        self.number = number
        self.angle = angle
        self.start = start
        self.end = end
        self.delay = 1

    def spin(self):
        kit.servo[self.number].angle = self.start
        time.sleep(self.delay)
        kit.servo[self.number].angle = self.end
        time.sleep(self.delay)
        kit.servo[self.number].angle = self.start
        time.sleep(self.delay)

def servo_activate(pin, angle, start, end):
    this_servo = Servo(pin, angle, start, end)
    
    this_servo.spin()
    
if __name__ == "__main__":
    t1 = threading.Thread(target=servo_activate, args=(4, 90, 0 , 100))
    t2 = threading.Thread(target=servo_activate, args=(5, 90, 120 , 0))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")