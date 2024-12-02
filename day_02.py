import numpy as np

def is_safe(line):
    n = [int(x) for x in line.split()]
    v = np.array(n)
    d = np.diff(v)
    test1 = np.all(d > 0) or np.all(d < 0)
    test2 = np.all(np.abs(d) >= 1) and np.all(np.abs(d) <= 3)
    return test1 and test2

def count_safe(input_data):
    lines = input_data.strip().split('\n')
    safe_reports = [line for line in lines if is_safe(line.strip())]
    return len(safe_reports)

with open('input.txt', 'r') as file:
    input_data = file.read()

with open('input_example.txt', 'r') as file:
    input_example_data = file.read()

print(f'part1: {count_safe(input_example_data)} {count_safe(input_data)}')


def is_safe2(line):
    if is_safe(line):
        return True
    
    n = len(line.split())
    for i in range(n):
        new_line = ' '.join(line.split()[:i] + line.split()[i+1:])
        if is_safe(new_line):
            return True
    return False

def count_safe2(input_data):
    lines = input_data.strip().split('\n')
    safe_reports = [line for line in lines if is_safe2(line.strip())]
    return len(safe_reports)

print(f'part2: {count_safe2(input_example_data)} {count_safe2(input_data)}')
