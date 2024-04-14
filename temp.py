# imports
#import movelib
import solver as sv

# GUI menu opetions
'''
1. Enter the colors of your cube
2. Enter the current colors of your cube
3. Set megacube to your cube
4. Make megacube solve
5. Make megacube scramble
6. Make megacube reset
7. Exit
'''

# global variables



# method 1

def set_colors():
    solve_colors = ['U', 'R', 'F', 'D', 'L', 'B']
    cube_colors = {}

    for color in solve_colors:
        print(f'Enter the colors of the cube {color}:  ') # Y R B W O G
        cube_colors[input()] = color



# main loop

while True:
    print('''
    1. Enter the colors of your cube
    2. Enter the current colors of your cube
    3. Set megacube to your cube
    4. Make megacube solve
    5. Make megacube scramble
    6. Make megacube reset
    7. Exit
    ''')
    choice = input('Enter your choice:  ')
    if choice == '1':
        set_colors()
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        break
    else:
        print('Invalid choice')
        continue
