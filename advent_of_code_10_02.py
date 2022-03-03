def calc_line_score(opensigns):
    total_score = 0
    score = {'(': 1, '[': 2, '{': 3, '<': 4}
    for opensign in reversed(opensigns):
        total_score = total_score*5 + score[opensign]
    return total_score


with open('inputs/input_10_01.txt') as f:
    lines = [list(x) for x in f.read().split('\n')]

pair = {')': '(', ']': '[', '>': '<', '}': '{'}
score_list = []

for line in lines:
    traveled_opensigns = []
    for sign in line:
        if sign in ('[', '(', '<', '{'):
            traveled_opensigns.append(sign)
        elif traveled_opensigns[-1] == pair[sign]:
            traveled_opensigns.pop()
        else:
            break
    if traveled_opensigns:
        score_list.append(calc_line_score(traveled_opensigns))

med = int(len(score_list) / 2)
print(sorted(score_list)[med])
# 1190420163
