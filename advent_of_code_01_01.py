values = []
count = 0

with open('inputs/input_01_01.txt') as f:
    for line in f:
        values.append(int(line.strip()))

sum_a = values[0] + values[1] + values[2]

for i, value in enumerate(values):
    if i < 2: continue
    sum_b = values[i-2] + values[i-1] + values[i]
    count = count + 1 if sum_b > sum_a else count
    sum_a = sum_b

print(count)