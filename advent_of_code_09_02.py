def get_arounds(pos, h_map):
    y, x = pos
    height = len(h_map)
    width = len(h_map[0])
    to_check = []
    if x > 0:
        to_check.append((y, x - 1))
    if x < width - 1:
        to_check.append((y, x + 1))
    if y > 0:
        to_check.append((y - 1, x))
    if y < height - 1:
        to_check.append((y + 1, x))
    return to_check

def around_in_basin(h_map, pos, visited):
    if(h_map[pos[0]][pos[1]]) == 9 or pos in visited:
        return 0
    visited.append(pos)
    count = 1
    yx_to_check = get_arounds(pos, h_map)
    for yx in yx_to_check:
        count += around_in_basin(h_map, yx, visited)
    return count


visited = []
basins = []
with open('inputs/input_09_01.txt') as f:
    h_map = [list(x) for x in f.read().split('\n')]
for y, row in enumerate(h_map):
    h_map[y] = [int(a) for a in row]

for y, row in enumerate(h_map):
    for x, element in enumerate(row):
        yx_to_check = get_arounds((y, x), h_map)
        values = [h_map[el[0]][el[1]] for el in yx_to_check]
        if element < min(values):
            size = around_in_basin(h_map, (y, x), visited)
            basins.append(size)

basins = sorted(basins)
print(basins[-3] * basins[-2] * basins[-1])
#827904





