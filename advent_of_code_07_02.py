def get_distances(check_val, positions):
    distances = []
    for position in positions:
        a_n = abs(check_val - position)
        n = a_n + 1
        distances.append(int(a_n / 2 * n))
    return distances

with open('inputs/input_07_01.txt') as f:
    for i, line in enumerate(f):
        positions = [int(x) for x in line.strip().split(',')]

min_sum = 10 ** 30
positions.sort()
min_val = positions[0]
max_val = positions[-1]

for i in range(min_val, max_val):
    cur_dist_sum = sum(get_distances(i, positions))
    min_sum = cur_dist_sum if cur_dist_sum < min_sum else min_sum

print(min_sum)

# middleValue -> positions[834] = 992






