class Section:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def sign(n):
    return int(n / abs(n) if n != 0 else 0)


def mark_section(array, section):
    dist_hor = section.p2[0] - section.p1[0]
    dist_ver = section.p2[1] - section.p1[1]
    start_x = section.p1[0]
    start_y = section.p1[1]
    marked_count = 0
    for i in range(max(abs(dist_hor), abs(dist_ver))+1):
        offset_y = i * sign(dist_ver)
        offset_x = i * sign(dist_hor)
        array[start_y + offset_y][start_x + offset_x] += 1
        if array[start_y + offset_y][start_x + offset_x] == 2:
            marked_count += 1
    return marked_count


array = [[0] * 1000 for _ in range(1000)]
sections = []
count = 0

with open('inputs/input_01_05.txt') as f:
    for i, line in enumerate(f):
        p = line.strip().split(' -> ')
        p1 = [int(x) for x in p[0].split(',')]
        p2 = [int(x) for x in p[1].split(',')]
        sections.append(Section(p1, p2))

for section in sections:
    count += mark_section(array, section)

print(count)
# 18144