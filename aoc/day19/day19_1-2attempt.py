import re

with open("day19_inputs_entries.txt") as f:
    entries = f.readlines()

with open("day19_input_rules.txt") as f:
    rules = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
entries = [x.strip() for x in entries]
rules = [x.strip() for x in rules]


# rules = ["0: 1 2", "1: \"a\"", "2: 1 3 | 3 1", "3: \"b\""]
# entries = ["aaa", "aab", "baa"]


# rules = ["0: 4 1 5", "1: 2 3 | 3 2", "2: 4 4 | 5 5", "3: 4 5 | 5 4", "4: \"a\"", "5: \"b\""]
# entries = ["ababbb", "bababa", "abbbab", "aaabbb", "aaaabbb"]


def generate_rule_map(rules_list):
    rules_map = {}
    for rule in rules_list:
        split_rule = rule.split(":")
        rules_map[split_rule[0]] = split_rule[1].strip()

    return rules_map


rules_map = generate_rule_map(rules)


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def process_rule(rule):
    result_rule = ""
    rule_split = rule.split(" ")
    for split in rule_split:
        if has_numbers(split):
            rule_output = rules_map[split.strip()]
            if rule_output.__contains__("|"):
                result_rule += " ( " + rule_output + " ) "
            else:
                result_rule += " " + rule_output.replace("\"", "") + " "
        else:
            result_rule += " " + split + " "

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
