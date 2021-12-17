with open('inputs/input_06_01.txt') as f:
    for i, line in enumerate(f):
        fishes = [int(x) for x in line.strip().split(',')]

for day in range(18):
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            fishes.append(8)
            continue
        fishes[i] -= 1

print(len(fishes))
# 386640