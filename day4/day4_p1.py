import timeit
import sys

f = 'input_day4.txt'

count = sum(
    [
        1 if (
            (
                assignments[0] >= assignments[2] 
                and 
                assignments[1] <= assignments[3]
            ) 
            or 
            (
                assignments[0] <= assignments[2] 
                and 
                assignments[1] >= assignments[3]
            ) 
        ) else 0 
        for assignments in 
        [
            list(
                map(int, line.replace("-",",").split(","))
            ) 
            for line in open(f,'r').read().splitlines()
        ]
    ]
)

print(f'count: {count}')

###################################################################
# Check that we're within 50% of the expected time for O(n) runtime
###################################################################

def oneline_sans_file_open(input):
    return sum([1 if ((assignments[0] >= assignments[2] and assignments[1] <= assignments[3]) or (assignments[0] <= assignments[2] and assignments[1] >= assignments[3]) ) else 0 for assignments in [list(map(int, line.replace("-",",").split(","))) for line in input ]])

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
result = "Yay!" if variance < 0.50 else "Boo!"
print(f'Variance is {variance:.2%} {result}')

