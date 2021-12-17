count = 0
with open('inputs/input_08_01.txt') as f:
    for i, line in enumerate(f):
        out_val = line.split('|')[1].strip().split(' ')
        for val in out_val:
            if len(val) in (2, 3, 4, 7):
                count += 1

print(count)
#543







