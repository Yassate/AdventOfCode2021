def str_in_str(checked, known):
    all_in = True
    for char in known:
        all_in = all_in and (char in checked)
    return all_in

def str_minus_str(input_str, subtract):
    for char in subtract:
        input_str = input_str.replace(char, '')
    return input_str


numbers = [''] * 10
count = 0

with open('inputs/input_08_01.txt') as f:
    for line in f:
        seq_dict = dict()
        right_side_number = 0
        left_side = sorted(line.split('|')[0].strip().split(' '), key=len)
        left_side = [''.join(sorted(x)) for x in left_side]
        right_side = line.split('|')[1].strip().split(' ')
        right_side = [''.join(sorted(x)) for x in right_side]
        five_segments = left_side[3:6]
        six_segments = left_side[6:9]
        numbers[1] = left_side[0]
        numbers[4] = left_side[2]
        numbers[7] = left_side[1]
        numbers[8] = left_side[9]
        numbers[3] = next(filter(lambda x: str_in_str(x, numbers[1]), five_segments))
        numbers[9] = next(filter(lambda x: str_in_str(x, numbers[3]), six_segments))
        seg_1 = str_minus_str(numbers[9], numbers[3])
        seg_4 = str_minus_str(numbers[4], numbers[1]).replace(seg_1, '')
        seg_5 = str_minus_str(numbers[8], numbers[9])
        numbers[0] = next(filter(lambda x: not str_in_str(x, seg_4), six_segments))
        numbers[2] = next(filter(lambda x: str_in_str(x, seg_5), five_segments))
        numbers[5] = next(filter(lambda x: str_in_str(x, seg_1), five_segments))
        numbers[6] = next(filter(lambda x: x != numbers[0] and x != numbers[9], six_segments))
        for i, number in enumerate(numbers):
            seq_dict[number] = i
        for i, id_str in enumerate(reversed(right_side)):
            right_side_number += seq_dict[id_str] * 10 ** i
        count += right_side_number

print(count)
#994266







