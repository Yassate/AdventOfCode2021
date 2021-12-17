class Fish:
    def __init__(self, start_day, lifetime):
        self.lifetime = lifetime
        self.start_day = start_day

    def count_family(self):
        count = 1
        for day_no in range(self.start_day, self.lifetime, 7):
            child = Fish(8, self.lifetime - day_no - 1)
            count += child.count_family()
        #print(count)
        return count

with open('inputs/input_06_01.txt') as f:
    for i, line in enumerate(f):
        fishes = [int(x) for x in line.strip().split(',')]

days_ = 16
count_all = 0

for days in range(days_):
    for fish_days in fishes:
        cur_fish = Fish(fish_days, days)
        count_all += cur_fish.count_family()
        print((days,count_all))







