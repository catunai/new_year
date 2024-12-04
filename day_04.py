import numpy as np

with open('input_example.txt', 'r') as f:
    input_string_example = f.read()

with open('input.txt', 'r') as f:
    input_string = f.read()

lines = []
for line in input_string.strip().split('\n'):
    lines.append(list(line))
x = np.array(lines)
rows, cols = x.shape

# count horizontal going right direction only xD
def count_h(x):
    ct = 0
    for r in range(rows):
        for c in range(cols - 3):
            if ''.join(x[r, c:(c+4)]) == 'XMAS':
                ct += 1
    return(ct)

# count along right diagonal going right direction only xD
def count_d(x):
    ct = 0
    for r in range(rows - 3):
        for c in range(cols - 3):
            if ''.join(np.diag(x[r:(r+4), c:(c+4)])) == 'XMAS':
                ct += 1
    return(ct)

# count both
def count_hd(x):
    return count_h(x) + count_d(x)

# rotate the matrix
def rotate(x):
    return x.T[::-1,:]

def count_all(x):
    n = 0
    for i in range(4):
        n += count_hd(x)
        x = rotate(x)
    return n

print(f'part1: {count_all(x)}')

def count_xmas(x):
    ct = 0
    for r in range(rows-2):
        for c in range(cols-2):
            z = x[r:(r+3), c:(c+3)]
            if z[1,1] == 'A':
                if set((z[0,0],z[2,2])) == set(('M','S')):
                    if set((z[0,2],z[2,0])) == set(('M','S')):
                        ct += 1
    return ct

print(f'part2: {count_xmas(x)}')
