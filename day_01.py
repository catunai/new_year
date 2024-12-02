import numpy as np
import pandas as pd

def convert_to_csv(input_file):
    output_file = input_file.replace('.txt', '.csv')

    lines_out = []
    with open(input_file, 'r') as f:
        for line in f:
            lines_out.append(','.join(line.strip().split()))

    with open(output_file, 'w') as f:
        for line in lines_out:
            f.write(line + '\n')
    
    return output_file

def part1(input_csv):
    data = pd.read_csv(input_csv, header=None)

    v1 = data[0].values
    v2 = data[1].values

    v1_sorted = np.sort(v1)
    v2_sorted = np.sort(v2)

    s = np.abs(v1_sorted - v2_sorted).sum()

    return s

input_example_file = 'input_example.txt'
input_file = 'input.txt'

input_example_csv = convert_to_csv(input_example_file)
input_csv = convert_to_csv(input_file)

print(f'part1: {part1(input_example_csv)} {part1(input_csv)}')

def part2(input_csv):
    data = pd.read_csv(input_csv, header=None)

    cts = data.groupby(1).count().reset_index()
    cts.columns = [0, 2]

    data = data[[0]].merge(cts)
    s = np.dot(data[0].values, data[2].values)

    return s

print(f'part2: {part2(input_example_csv)} {part2(input_csv)}')
