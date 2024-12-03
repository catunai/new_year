import re

with open('input_example.txt', 'r') as f:
    input_string_example = f.read()

with open('input_example2.txt', 'r') as f:
    input_string_example2 = f.read()

with open('input.txt', 'r') as f:
    input_string = f.read()

def extract_mul(s):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(pattern, s)
    total = 0
    for m in matches:
        nums = m[4:-1].split(',')
        total += int(nums[0]) * int(nums[1])
    return total

def extract_block(s):
    s = s.replace("\n", "")
    s = "do()" + s + "don't()"
    pattern = r"do\(\).*?don't\(\)"
    matches = re.findall(pattern, s)
    total = 0
    for m in matches:
        total += extract_mul(m)
    return total

print(f'part1: {extract_mul(input_string_example)} {extract_mul(input_string)}')
print(f'part2: {extract_block(input_string_example2)} {extract_block(input_string)}')
