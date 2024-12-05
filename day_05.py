import itertools

with open('input.txt', 'r') as f:
    input_string = f.read()

input_rules, input_updates = input_string.strip().split('\n\n')
updates = input_updates.split('\n')

rules_set = set(input_rules.split('\n'))

def test_update(u):
    r = range(len(u))
    rule_breaks = [f'{u[j]}|{u[i]}' for i, j in itertools.product(r, r) if i < j]
    return set(rule_breaks).intersection(rules_set) == set()

def sum_good(updates):
    s = 0
    for update in updates:
        u = list(map(int, update.split(',')))
        if test_update(u):
            s += u[len(u) // 2]
    return s
        
print(f'part1: {sum_good(updates)}')

# Gotta assume that rules is not inconsistent 
# and complete to define totally ordered set
# Cuz otherwise asking for middle number doesn't make sense
# So first order buble sort should do it ^_^
def sort_update(u):
    was_sorted = True
    for i in range(len(u)-1):
        if f'{u[i+1]}|{u[i]}' in rules_set:
            x = u[i]
            u[i] = u[i+1]
            u[i+1] = x
            was_sorted = False
    if not was_sorted:
        return sort_update(u)
    return u

def sum_bad(updates):
    s = 0
    for update in updates:
        u = list(map(int, update.split(',')))
        if not test_update(u):
            u = sort_update(u)
            s += u[len(u) // 2]
    return s

print(f'part2: {sum_bad(updates)}')