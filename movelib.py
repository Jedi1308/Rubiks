import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

dir_pins = [20, 5]
step_pins = [21, 6]
EN_pin = 24

def turn_cw_360(face):
    mymotor = RpiMotorLib.A4988Nema(dir_pins[face], step_pins[face], (21, 21, 21), "A4988")
    GPIO.setup(EN_pin, GPIO.OUT)
    GPIO.output(EN_pin, GPIO.LOW)
    mymotor.motor_go(True, "1/16", 200, .0044, True, .05)

def turn_ccw_360(face):
    mymotor = RpiMotorLib.A4988Nema(dir_pins[face], step_pins[face], (21, 21, 21), "A4988")
    GPIO.setup(EN_pin, GPIO.OUT)
    GPIO.output(EN_pin, GPIO.LOW)
    mymotor.motor_go(False, "1/16", 200, .0044, True, .05)

def turn_cw_90(face):
    mymotor = RpiMotorLib.A4988Nema(dir_pins[face], step_pins[face], (21, 21, 21), "A4988")
    GPIO.setup(EN_pin, GPIO.OUT)
    GPIO.output(EN_pin, GPIO.LOW)
    mymotor.motor_go(True, "1/16", 50, .0044, True, .05)

def turn_ccw_90(face):
    mymotor = RpiMotorLib.A4988Nema(dir_pins[face], step_pins[face], (21, 21, 21), "A4988")
    GPIO.setup(EN_pin, GPIO.OUT)
    GPIO.output(EN_pin, GPIO.LOW)
    mymotor.motor_go(False, "1/16", 50, .0044, True, .05)

    