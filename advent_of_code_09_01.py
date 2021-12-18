count = 0
with open('inputs/input_09_01.txt') as f:
    h_map = [list(x) for x in f.read().split('\n')]
for y, row in enumerate(h_map):
    h_map[y] = [int(a) for a in row]

for y, row in enumerate(h_map):
    for x, element in enumerate(row):
        v_to_check = []
        if x > 0:
            v_to_check.append(h_map[y][x-1])
        if x < len(row)-1:
            v_to_check.append(h_map[y][x+1])
        if y > 0:
            v_to_check.append(h_map[y-1][x])
        if y < len(h_map)-1:
            v_to_check.append(h_map[y+1][x])
        if element < min(v_to_check):
            count += element + 1
print(count)
#585






