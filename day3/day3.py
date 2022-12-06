import timeit
import sys

f = 'input_day2.txt'
# f = 'test.txt'

count = sum([sum(set([i for i in side_1 if i in side_2])) for side_1, side_2 in [[rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):]] for rucksack in [[ord(char) - 96 if char.islower() else abs(ord(char) - 38) for char in line] for line in open(f,'r').read().splitlines()]]])

print(f'count: {count}')

###################################################################
# Check that we're within 50% of the expected time for O(n) runtime
###################################################################

input = open(f,'r').read().splitlines()
def oneline_sans_file_open(input):
    return sum([sum(set([i for i in side_1 if i in side_2])) for side_1, side_2 in [[rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):]] for rucksack in [[ord(char) - 96 if char.islower() else abs(ord(char) - 38) for char in line] for line in input]]])

n = open(f,'r').read().splitlines()
scaling_factor = 10
n_scaled = n * scaling_factor
f1 = 'oneline_sans_file_open(n)'
f2 = 'oneline_sans_file_open(n_scaled)'
func = 'oneline_sans_file_open'
def get_variance(f1, f2, iter):
    input_time_n = timeit.timeit(f1, number=iter, globals=globals())
    input_time_n_scaled = timeit.timeit(f2, number=iter, globals=globals())
    input_time_n_expected = input_time_n_scaled / scaling_factor
    return abs((input_time_n / input_time_n_expected) - 1) 

variance = get_variance(f1, f2, 100)
result = "Yay!" if variance < 0.50 else "Boo!"
print(f'Variance is {variance:.2%} {result}')

