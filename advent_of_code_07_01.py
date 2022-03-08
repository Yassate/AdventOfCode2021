with open('inputs/input_07_01.txt') as f:
    for i, line in enumerate(f):
        positions = [int(x) for x in line.strip().split(',')]

positions.sort()
median = positions[500]
distances = [abs(x-median) for x in positions]

print(sum(distances))
# 349812





