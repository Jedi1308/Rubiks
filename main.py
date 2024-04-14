


solve_colors = ['U', 'R', 'F', 'D', 'L', 'B']
cube_colors = {}

for color in solve_colors:
    print(f'Enter the colors of the cube {color}:  ') # Y R B W O G
    cube_colors[input()] = color

unsolved = ''
for color in cube_colors.keys():
    unsolved += input(f'Enter the colors of the {color} face (left-right, top-down):  ')
    
unsolved_translated = ''
for color in unsolved:
    unsolved_translated += cube_colors[color]

print(unsolved_translated)

solution = sv.solve(unsolved_translated)
print(solution)







