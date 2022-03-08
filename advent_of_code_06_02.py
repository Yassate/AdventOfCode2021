with open('inputs/input_06_01.txt') as f:
    for i, line in enumerate(f):
        fish = [int(x) for x in line.strip().split(',')]

fish_count = []
for i in range(9):
    fish_count.append(fish.count(i))

for day in range(256):
    fish_count[7] += fish_count[0]
    fish_count.append(fish_count[0])
    fish_count.pop(0)

print(sum(fish_count))
# 1733403626279

# a hint from community were needed that 9 element list is enough to solve that problem






