import re

with open("day19_inputs_entries.txt") as f:
    entries = f.readlines()

with open("day19_input_rules.txt") as f:
    rules = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
entries = [x.strip() for x in entries]
rules = [x.strip() for x in rules]


# 96 - iteration 10	 after process 	19.541.404
# 48 - iteration 10	 after process 	 4.935.760


def generate_rule_map(rules_list):
    rules_map = {}
    for rule in rules_list:
        split_rule = rule.split(":")
        rules_map[split_rule[0]] = split_rule[1].strip()

    return rules_map


rules_map = generate_rule_map(rules)


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def space(string):
    return " " + string + " "


def recursive_output(step, step_output):
    step_output_split = step_output.split("|")
    result_step_output = ""
    for output_step in step_output_split:
        if output_step.__contains__(step):
            recursive_step = output_step
            temp_recursive_step = space(output_step.strip()).replace(space(step.strip()), " ")
            for recursive_index in range(1, max_entry_length):
                result_step_output += space(recursive_step).replace(space(step), space(temp_recursive_step))
                if recursive_index < max_entry_length - 1:
                    result_step_output += " | "
                recursive_step = space(recursive_step).replace(space(step), space(output_step))
        else:
            result_step_output += " " + output_step + " | "

        result_step_output = result_step_output.replace("  ", " ")

    result_step_output = result_step_output.strip()
    rules_map[step.strip()] = result_step_output
    return result_step_output


def process_rule(rule):
    result_rule = ""
    rule_steps = rule.split(" ")
    for step in rule_steps:
        if has_numbers(step):
            step_output = rules_map[step.strip()]
            if step_output.__contains__("|"):
                if space(step_output).__contains__(space(step)):
                    step_output = recursive_output(step, step_output)
                    result_rule += " ( " + step_output + " ) "
                else:
                    result_rule += " ( " + step_output + " ) "
            else:
                result_rule += " " + step_output.replace("\"", "") + " "
        else:
            result_rule += " " + step + " "

    return result_rule.replace("  ", " ").strip()


def process():
    global current_rule

    iteration = 0
    while has_numbers(current_rule):
        print("iteration " + str(iteration) + "\t befor process \t" + str(len(current_rule)))
        current_rule = process_rule(current_rule)
        print("iteration " + str(iteration) + "\t after process \t" + str(len(current_rule)))
        print("")

        iteration += 1


max_entry_length = -1
for entry in entries:
    if len(entry) > max_entry_length:
        max_entry_length = len(entry)
max_entry_length = int(max_entry_length / 2)

current_rule = "0"
process()


def clean_rule():
    global current_rule

    current_rule = current_rule.replace(" ", "")


clean_rule()


def count_valid_messages(messages):
    count = 0
    for message in messages:
        if re.search("^" + current_rule + "$", message):
            count += 1

    return count


print(count_valid_messages(entries))

exit(0)
