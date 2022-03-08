with open('inputs/input_06_01.txt') as f:
    for i, line in enumerate(f):
        fish = [int(x) for x in line.strip().split(',')]

for day in range(18):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
            continue
        fish[i] -= 1

print(len(fish))
# 386640