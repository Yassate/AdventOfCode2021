aim, vert, hor = 0, 0, 0

with open('inputs/input_01_02.txt') as f:
    for line in f:
        direction, value = line.strip().split()
        value = int(value)
        if direction == 'forward':
            vert = vert + value * aim
            hor = hor + value
        else:
            aim = aim + value if direction == 'down' else aim - value

print(vert * hor)
#1739283308