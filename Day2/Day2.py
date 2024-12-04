input_data = "input.txt"

with open(input_data, "r") as file:
    data_report = file.readlines()

data = []
for line in data_report:
    number = line.strip().split(' ')
    row = [int(num) for num in number]
    data.append(row)

def strict_pattern(row):
    increasing = all(row[i] < row[i+1] for i in range(len(row)-1))
    decreasing = all(row[i] > row[i+1] for i in range(len(row)-1))
    return increasing, decreasing

def safe_row(row):
    increasing, decreasing = strict_pattern(row)
    if increasing:
        return all(1 <= row[i+1] - row[i] <= 3 for i in range(len(row)-1))
    elif decreasing:
        return all(-3 <= row[i+1] - row[i] <= -1 for i in range(len(row)-1))
    return False

def report_safety(data):
    counter = 0
    for row in data:
        if safe_row(row):
            counter += 1
        elif damper_tool(row):
            counter += 1
    return counter

def damper_tool(row):
    for i in range(len(row)):
        edited_row = row[:i] + row[i+1:]
        if safe_row(edited_row):
            return True
    return False

safe_counter = report_safety(data)
print("safe counter: " + str(safe_counter))
