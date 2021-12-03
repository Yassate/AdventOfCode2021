def filter_out(values, a, bin_value):
    sum = 0
    for value in values:
        sum = sum + int(value[a])
    dominant = str(bin_value) if sum < len(values) / 2 else str(abs(bin_value - 1))
    result = [value for value in values if value[a] == dominant]
    return int(values[0], 2) if len(values) == 1 else filter_out(result, a + 1, bin_value)


with open('inputs/input_01_03.txt') as f:
    values = f.readlines()

val1 = filter_out(values, 0, 1)
val2 = filter_out(values, 0, 0)

print(val1 * val2)
#2817661