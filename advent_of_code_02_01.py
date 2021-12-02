vert, hor = 0, 0

with open('inputs/input_01_02.txt') as f:
    for line in f:
        direction, value = line.strip().split()
        value = int(value)
        if direction == 'forward':
            vert = vert + value
        else:
            hor = hor + value if direction == 'down' else hor - value

print(hor*vert)
#1815044