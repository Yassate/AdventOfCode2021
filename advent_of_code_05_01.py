class Section:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


def mark_section(array, section):
    marked_count = 0
    start_x = min(section.p1[0], section.p2[0])
    start_y = min(section.p1[1], section.p2[1])
    dist_hor = abs(section.p1[0] - section.p2[0]) + 1
    dist_ver = abs(section.p1[1] - section.p2[1]) + 1
    for offset_x in range(dist_hor):
        for offset_y in range(dist_ver):
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
        if p1[0] == p2[0] or p1[1] == p2[1]:
            sections.append(Section(p1, p2))

for section in sections:
    count += mark_section(array, section)

print(count)
#5576