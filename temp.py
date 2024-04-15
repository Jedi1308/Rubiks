import kociemba
import os
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

# global solve variables

solve_colors = ['U', 'R', 'F', 'D', 'L', 'B']
cube_colors = {}

unsolved = ''
solution = ''
solved = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
goal_state = ''
message = ''

# global motor variables

dir_pins = [20, 5]
step_pins = [21, 6]
EN_pin = 24

type_switch = {
    1: 50,
    2: 100,
    3: 50
}

# motor move function
def motor_move(face, num):
    degrees = type_switch[num] 
    mymotor = RpiMotorLib.A4988Nema(dir_pins[face], step_pins[face], (-1, -1, -1), "A4988")
    GPIO.setup(EN_pin, GPIO.OUT)
    GPIO.output(EN_pin, GPIO.LOW)
    mymotor.motor_go(num != 3, "Full", degrees, .001, True, .05)
    print()

# cube go

def cube_go(moves):
    global message

    if len(moves) == 54:
        message = 'Invalid moveset'
        return
    
    moves = moves[0:-3]
    message =  moves

# option 1
def set_colors():
    global message, cube_colors

    cube_colors.clear()

    default = input('Default colors? (YRBWOG)')

    if default == 'Y':
        cube_colors = {'Y'}
    elif default == 'N':
        for color in solve_colors:
            print(f'Enter the colors of the cube {color}:  ') # Y R B W O G
            cube_colors[input()] = color
    else:
        message = 'Invalid option'
        return

    message = 'Cube colors set'

# option 2
def enter_cube_state():
    global message, unsolved

    if not cube_colors:
        message = 'Colors for your cube are not set'
        return
    for color in cube_colors.keys():
        unsolved += input(f'Enter the colors of the {color} face (left-right, top-down):  ')
        message = 'Cube state set'

# option 3
def create_solution():
    global message, unsolved, solution

    if len(unsolved) != 54:
        message = 'Cube entered incorrectly'
        return
    solution = kociemba.solve(unsolved)
    message = 'Cube solution stored'

# option 4
def match_cube():
    global message, unsolved
    if len(unsolved) != 54:
        message = 'Cube entered incorrectly'
        return
    temp_matching = kociemba.solve(solved, unsolved)
    cube_go(temp_matching)
    message = 'Megacube set'

# main loop
while True:
    os.system('clear')
    
    print('''Welcome to the Megacube!
    1. Enter the colors of your cube
    2. Enter your cube state
    3. Get your cube state solution
    4. Set megacube to your cube
    5. Make megacube solve
    6. Make megacube scramble
    7. Exit
    ''')

    if message != '':
        print('MESSAGE: ' + message)
        print()

    message = ''

    choice = input('Enter your choice:  ')
    if choice == '1':
        set_colors()
    elif choice == '2':
        enter_cube_state()
    elif choice == '3':
        create_solution()
    elif choice == '4':
        match_cube()
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        break
    else:
        print('Invalid choice')
        continue
