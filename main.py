import kociemba
import os
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

# global solve variables

solve_colors = ['U', 'R', 'F', 'D', 'L', 'B']
cube_colors = {}

unsolved = ''
solution = ''
to_match = ''
solved = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
goal_state = ''
message = ''

# global motor variables

dir_pins = [20, 5]
step_pins = [21, 6]
EN_pin = 24

step_switch = {
    1: 50,
    2: 100,
    3: 50
}

# motor move function
def motor_move(face, num):
    degrees = step_switch[num] 
    mymotor = RpiMotorLib.A4988Nema(dir_pins[face], step_pins[face], (-1, -1, -1), "A4988")
    GPIO.setup(EN_pin, GPIO.OUT)
    GPIO.output(EN_pin, GPIO.LOW)
    mymotor.motor_go(num != 3, "Full", degrees, .001, True, .05)
    print()

# cube go TODO elements for options 4 + 5
def cube_go(arg):
    global message

    s = ''
    # solve arg for option 5
    if arg == 0:
        s = solution
    # match arg for option 4
    elif arg == 1:
        s = kociemba.solve(solved, unsolved)

    moveset = s.split(' ')
    for move in moveset:
        motor_move(0, 2)

    # TODO map function to get moves from face and num e.g. R' or B or F2

    if arg == 0:
        message = 'Cube solved!'
    elif arg == 1:
        message = 'Moveset to match: ' + s

# option 1
def set_colors():
    global message, cube_colors

    cube_colors.clear()

    default = input('Default colors (set to YRBWOG)? [Y/N]: ')

    if default == 'Y': 
        cube_colors = {'Y': 'U', 'R': 'R', 'B': 'F', 'W': 'D', 'O': 'L', 'G': 'B'}
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
    unsolved_translated = ''
    for color in unsolved:
        unsolved_translated += cube_colors[color]    
    unsolved = unsolved_translated
    message = 'Cube state set: ' + unsolved

# option 3
def create_solution():
    global message, unsolved, solution

    if len(unsolved) != 54:
        message = 'Cube entered incorrectly'
        return
    solution = kociemba.solve(unsolved)
    message = 'Cube solution stored'

# TODO option 4 add to cube_go
def match_cube():
    global message, unsolved
    if len(unsolved) != 54:
        message = 'Cube entered incorrectly'
        return
    temp_matching = kociemba.solve(solved, unsolved)
    message = cube_go(temp_matching)
    message = 'Megacube set by ' + temp_matching

# TODO ^

# TODO option 6 scramble generator
def scramble():
    return


# main loop
while True:
    os.system('clear')
    
    print('''Welcome to the Megacube!
    1. Enter the colors of your cube
    2. Enter your cube state
    3. Create cube state solution
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
        cube_go(1)
    elif choice == '5':
        cube_go(0)
    elif choice == '6':
        scramble()
    elif choice == '7':
        print('Goodbye!')
        break
    else:
        message = 'Invalid choice'
        continue