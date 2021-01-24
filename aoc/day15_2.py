entries = [1, 20, 8, 12, 0, 14]


# entries = [0, 3, 6]  # 175594
# entries = [1, 3, 2]  # 2578
# entries = [2, 1, 3]  # 3544142
# entries = [1, 2, 3]  # 261214
# entries = [2, 3, 1]  # 6895259
# entries = [3, 2, 1]  # 18
# entries = [3, 1, 2]  # 362


def obtain_number(memory, number, age):
    result = 0

    if number in memory:
        result = age - memory[number]

    memory[number] = age
    return result


memory = {}
new_number = 0
age = len(entries)
stopping_point = 30000000

for index, entry in enumerate(entries, start=1):
    new_number = obtain_number(memory, entry, index)

while age <= stopping_point:
    age += 1
    if age == stopping_point:
        break
    new_number = obtain_number(memory, new_number, age)

print(new_number)
exit(0)
