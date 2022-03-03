with open('inputs/input_07_01.txt') as f:
    for i, line in enumerate(f):
        positions = [int(x) for x in line.strip().split(',')]

positions.sort()
print(positions)
median = positions[500]

distances = [abs(x-median) for x in positions]
distances.sort()
new_median = median + distances[500]
new_distances = [(1+abs(x-new_median))/2*abs(x-new_median) for x in positions]
print(distances[500])
print(median)
print(distances)
print(sum(new_distances))






