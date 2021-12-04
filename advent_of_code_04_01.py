values = []
epsilon = gamma = ''

with open('inputs/input_01_03.txt') as f:
    values = f.readlines()

for a in range(11):
    sum = 0
    for value in values:
        sum = sum + int(value[a])
    gamma = gamma + '1' if sum > len(values) / 2 else gamma + '0'
    epsilon = epsilon + '0'if sum > len(values) / 2 else epsilon + '1'

print(int(gamma, 2)*int(epsilon, 2))
#508062
