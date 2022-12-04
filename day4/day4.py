import timeit
import sys

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

inp = open('input_day4.txt','r').read().splitlines()
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

oneline_count = sum([1 if ((lst[0] >= lst[2] and lst[1] <= lst[3]) or (lst[0] <= lst[2] and lst[1] >= lst[3]) ) else 0 for lst in [list(map(int, line.replace("-",",").split(","))) for line in open('input_day4.txt','r').read().splitlines()]])
print(f'oneline_count: {oneline_count}')

def big_O_test(inp4):
    return sum([1 if ((lst[0] >= lst[2] and lst[1] <= lst[3]) or (lst[0] <= lst[2] and lst[1] >= lst[3]) ) else 0 for lst in [list(map(int, line.replace("-",",").split(","))) for line in inp4 ]])

single = open('input_day4.txt','r').read().splitlines()
ten = single * 10
iterations = 100
single_input_time = timeit.timeit("big_O_test(single)", number=iterations, globals=globals())
ten_input_time = timeit.timeit("big_O_test(ten)", number=iterations, globals=globals())
single_input_time_expected = ten_input_time / 10
variance = abs((single_input_time / single_input_time_expected) - 1) 
print(variance)

