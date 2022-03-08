def get_dists(check_val, positions):
    distances = []
    for position in positions:
        a_n = abs(check_val - position)
        n = a_n + 1
        distances.append(int(a_n / 2 * n))
    return sum(distances)


with open('inputs/input_07_01.txt') as f:
    for i, line in enumerate(f):
        positions = [int(x) for x in line.strip().split(',')]

min_sum = 2 ** 32

for i in range(min(positions), max(positions)):
    cur_dists_sum = get_dists(i, positions)
    min_sum = cur_dists_sum if cur_dists_sum < min_sum else min_sum

print(min_sum)
# 99763899






