entries = [1, 20, 8, 12, 0, 14]


# entries = [0, 3, 6]  # 436
# entries = [1, 3, 2]  # 1
# entries = [2, 1, 3]  # 10
# entries = [1, 2, 3]  # 27
# entries = [2, 3, 1]  # 78
# entries = [3, 2, 1]  # 438
# entries = [3, 1, 2]  # 1836


def obtain_number(memory, number, age):
    result = 0

    if number in memory:
        result = age - memory[number]

    memory[number] = age
    return result


memory = {}
new_number = 0
age = len(entries)

for index, entry in enumerate(entries, start=1):
    new_number = obtain_number(memory, entry, index)

while age <= 2020:
    age += 1
    if age == 2020:
        break
    new_number = obtain_number(memory, new_number, age)

print(new_number)
exit(0)
