import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

dir_pins = [20, 5]
step_pins = [21, 6]
EN_pin = 24

type_switch = {
    1: 50,
    2: 100,
    3: 50
}

def turn(face, num):
    degrees = type_switch[num] 
    mymotor = RpiMotorLib.A4988Nema(dir_pins[face], step_pins[face], (-1, -1, -1), "A4988")
    GPIO.setup(EN_pin, GPIO.OUT)
    GPIO.output(EN_pin, GPIO.LOW)
    mymotor.motor_go(num != 3, "Full", degrees, .001, True, .05)
    print()


print('ur mom')

while (True):
    a = int(input())
    b = int(input())
    turn(a, b)
    