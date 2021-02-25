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


def is_rule_processing_complete():
    global current_rules

    for rule in current_rules:
        if has_numbers(rule):
            return False

    return True


def process_rule(rule):
    rule_split = rule.split(" ")
    for split in rule_split:
        if has_numbers(split):
            rule_output = rules_map[split.strip()]
            if rule_output.__contains__("|"):
                rule_output_split = rule_output.split("|")
                for output_split in rule_output_split:
                    next_rule = (" " + rule + " ").replace(" " + split + " ", " " + output_split.strip() + " ", 1)
                    next_rules.append(next_rule.strip())
            else:
                next_rule = (" " + rule + " ") \
                    .replace(" " + split + " ", " " + rule_output.replace("\"", "").strip() + " ", 1)
                next_rules.append(next_rule.strip())

            break


def process_rules():
    global current_rules
    global next_rules

    iteration = 0
    while not is_rule_processing_complete():
        for rule in current_rules:
            if has_numbers(rule):
                process_rule(rule)
            else:
                next_rules.append(rule)

        print("iteration " + str(iteration) + "\t before deduplication \t" + str(len(next_rules)))
        current_rules = deduplicate_list(next_rules)
        next_rules = []
        print("iteration " + str(iteration) + "\t after deduplication \t" + str(len(current_rules)))
        iteration += 1


def deduplicate_list(duplicated_list):
    return list(dict.fromkeys(duplicated_list))


current_rules = ["0"]
next_rules = []
process_rules()


def clean_rules():
    global current_rules
    global next_rules

    for rule in current_rules:
        next_rules.append(rule.replace(" ", ""))

    current_rules = []
    for rule in next_rules:
        current_rules.append(rule)
    next_rules = []


clean_rules()


def count_valid_messages(messages):
    count = 0
    for message in messages:
        for rule in current_rules:
            if rule == message:
                count += 1
                break

    return count


print(count_valid_messages(entries))

exit(0)
