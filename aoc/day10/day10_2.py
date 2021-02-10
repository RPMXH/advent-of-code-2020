entries = [54, 91, 137, 156, 31, 70, 143, 51, 50, 18, 1, 149, 129, 151, 95, 148, 41, 144, 7, 125, 155, 14, 114, 108, 57,
           118, 147, 24, 25, 73, 26, 8, 115, 44, 12, 47, 106, 120, 132, 121, 35, 105, 60, 9, 6, 65, 111, 133, 38, 138,
           101, 126, 39, 78, 92, 53, 119, 136, 154, 140, 52, 15, 90, 30, 40, 64, 67, 139, 76, 32, 98, 113, 80, 13, 104,
           86, 27, 61, 157, 79, 122, 59, 150, 89, 158, 107, 77, 112, 5, 83, 58, 21, 2, 66]

# entries = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

# entries = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34,
#            10, 3]


def multiplier_calc(level):
    if level < 1:
        return 0
    if level <= 2:
        return level
    elif level == 3:
        return 4
    else:
        return multiplier_calc(level - 1) + multiplier_calc(level - 2) + multiplier_calc(level - 3)


entries.sort()
entries.append(max(entries) + 3)

diffs = [0] * (len(entries))
joltage = 0
index = 0
for entry in entries:
    diffs[index] += entry - joltage
    joltage = entry
    index += 1

consequent_one = 0
multiplier = 1
for diff in diffs:
    if diff == 1:
        consequent_one += 1

    elif diff > 1:
        multiplier = multiplier * multiplier_calc(max(consequent_one, 1))
        consequent_one = 0

print(multiplier)
