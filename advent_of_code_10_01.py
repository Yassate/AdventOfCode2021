with open('inputs/input_10_01.txt') as f:
    lines = [list(x) for x in f.read().split('\n')]

pair = {')': '(', ']': '[', '>': '<', '}': '{'}
score = {')': 3, ']': 57, '}': 1197, '>': 25137}

count = 0
traveled_opensigns = []
for line in lines:
    for sign in line:
        if sign in ('[', '(', '<', '{'):
            traveled_opensigns.append(sign)
        elif traveled_opensigns[-1] == pair[sign]:
            traveled_opensigns.pop()
        else:
            count += score[sign]
            break

print(count)
# 389589



