import timeit
import sys

f = 'input_day4.txt'

sample = [
    [94, 95, 61, 94],
    [38, 99, 39, 73], # yes 
    [6, 11, 11, 84], 
    [29, 49, 9, 29], 
    [24, 91, 24, 44], # yes
    [72, 72, 28, 72], # yes
    [28, 72, 72, 72], # yes
    [72, 72, 72, 72], # yes
    [49, 53, 49, 51], # yes
    [9, 85, 8, 85], # yes
    [26, 80, 26, 90] # yes
    ] # count should be 8 yes, 3 no

inp = open(f,'r').read().splitlines()
pairs = [list(map(int, line.replace("-",",").split(","))) for line in inp]
multiline_count = sum(
    [
        1 if (
            (lst[0] >= lst[2] and lst[1] <= lst[3]) or 
            (lst[0] <= lst[2] and lst[1] >= lst[3]) 
        ) else 0 for lst in pairs
    ]
)
print(f'multiline_count: {multiline_count}')

oneline_count = sum([1 if ((lst[0] >= lst[2] and lst[1] <= lst[3]) or (lst[0] <= lst[2] and lst[1] >= lst[3]) ) else 0 for lst in [list(map(int, line.replace("-",",").split(","))) for line in open(f,'r').read().splitlines()]])
print(f'oneline_count: {oneline_count}')

def oneline_sans_file_open(inp4):
    return sum([1 if ((lst[0] >= lst[2] and lst[1] <= lst[3]) or (lst[0] <= lst[2] and lst[1] >= lst[3]) ) else 0 for lst in [list(map(int, line.replace("-",",").split(","))) for line in inp4 ]])

# Check that we're within 10% of the expected time for O(n) runtime
n = open(f,'r').read().splitlines()
scalar = 10
n_scaled = n * scalar
f1 = 'oneline_sans_file_open(n)'
f2 = 'oneline_sans_file_open(n_scaled)'
func = 'oneline_sans_file_open'
def get_variance(f1, f2, iter):
    input_time_n = timeit.timeit(f1, number=iter, globals=globals())
    input_time_n_scaled = timeit.timeit(f2, number=iter, globals=globals())
    input_time_n_expected = input_time_n_scaled / scalar
    return abs((input_time_n / input_time_n_expected) - 1) 

variance = get_variance(f1, f2, 100)
print(f'Variance is {variance}')
result = "Yay!" if variance < 0.50 else "Boo!"
print(f'Variance is {variance:.2%} {result}')

