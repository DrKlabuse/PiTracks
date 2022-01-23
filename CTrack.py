# Pinbelegung
#   Motor 1
#     IN1   PIN 18  GPIO  24
#     IN2   PIN 16  GPIO  23
#     EN1   PIN 32  GPIO  12 (PWM0)
#   Motor 2
#     IN3   PIN 10  GPIO  15
#     IN4   PIN 8   GPIO  14
#     EN2   PIN 33  GPIO  13 (PWM1)

import RPi.GPIO as GPIO
import ITrack

class CTrack(ITrack.ITrack):

    GpioCtl1 = 0
    GpioCtl2 = 0
    GpioPwm = 0
    Dir = ITrack.ETrackDir.ETDIR_FORWARD
    Pwm = None

    def __init__(self, gpio_ctl1, gpio_ctl2, gpio_pwm):
        self.GpioCtl1 = gpio_ctl1
        self.GpioCtl2 = gpio_ctl2
        self.GpioPwm = gpio_pwm
        GPIO.setup(self.GpioCtl1, GPIO.OUT)
        GPIO.setup(self.GpioCtl2, GPIO.OUT)
        GPIO.setup(self.GpioPwm, GPIO.OUT)
        self.Pwm = GPIO.PWM(self.GpioPwm, 1000)
        self.Pwm.start(0)
        self.stop()

    def start(self):
        self.setDirection(self.Dir)

    def stop(self):
        GPIO.output(self.GpioCtl1, GPIO.LOW)
        GPIO.output(self.GpioCtl2, GPIO.LOW)

    def setDirection(self, dir):
        self.Dir = dir
        if(dir == ITrack.ETrackDir.ETDIR_FORWARD):
            GPIO.output(self.GpioCtl1, GPIO.LOW)
            GPIO.output(self.GpioCtl2, GPIO.HIGH)
        else:
            GPIO.output(self.GpioCtl1, GPIO.HIGH)
            GPIO.output(self.GpioCtl2, GPIO.LOW)

    def setSpeed(self, speed):
        self.Speed = speed
        self.Pwm.ChangeDutyCycle(speed)

    def cleanup(self):
        self.Pwm.stop()
