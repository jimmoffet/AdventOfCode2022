import timeit
import sys
import re

f = 'day5.txt'
# f = 'day5_test.txt'

top_crates = lambda f : [
    ''.join([
        final_stacks[0] for final_stacks in list(
            [ 
                (lambda _stacks_dict, _move_lines: 
                    [
                        (
                            _stacks_dict.update({ move[2]: 
                                _stacks_dict[ move[1] ][ : ( move[0] if move[0] <= len( _stacks_dict[ move[1] ] ) else -1 ) ][ : : -1 ] + _stacks_dict[ move[2] ]
                            }) 
                            != 
                            _stacks_dict.update({ move[1]: 
                                _stacks_dict[move[1]][int( len(_stacks_dict[move[1]][:(move[0] if move[0] <= len(_stacks_dict[move[1]]) else -1 ) ])  ):]
                            }) 
                        )
                        or _stacks_dict 
                        for move in _move_lines
                    ]
                )(stacks_dict, move_lines) 
                for stacks_dict, move_lines in 
                [
                    (
                        { k:list(filter((' ').__ne__, v)) for k,v in stack_lines.items() }, 
                        [ list(move.values())[0] for move in move_lines ]
                    ) 
                    for stack_lines, move_lines in 
                    [
                        (
                            {k: [dict[k] for dict in [all_lines[i] for i in range(0,8)]] for k in range(1,10)}, 
                            all_lines[10:]
                        ) # this is a two-item tuple
                        for all_lines in 
                        ([ 
                            { j+1: c for j,c in enumerate([L[1],L[5],L[9],L[13],L[17],L[21],L[25],L[29],L[33]]) } 
                            if i < 9 else 
                            { i: list(map(int, re.sub('[a-z]','',L).strip().split())) } 
                            if i > 10 else 
                            {i: None} 
                            for i, L in 
                            [ (i+1, line) for i, line in enumerate(open(f,'r').read().splitlines()) ]
                        ],) # this is a one-item tuple
                        
                    ]
                ]
            ][-1][-1].values()
        )
    ])
][0]

print(f'top_crates: {top_crates(f)}')

# NOTE: the ridiculous (s.update() != s.update()) which results in None != None, which evaluates to False, to force the lambda to return the updated dict s
# NOTE: parsing this input and operating on it in one line was... not a great developer experience
# NOTE: refactor moves as simple lists/tuples
# NOTE: o is the whole input
# NOTE: None is a bit of a hack, would be cool to be able to use something like continue in a list comprehension
# NOTE: enumerate(open()) to the rescue! Now I can parse and operate on the input in one line! :goto-10: :goto-10: :goto-10:
# NOTE: I do like that this one-liner constraint imposes quite a bit of ritual each day...

###################################################################
# Check that we're within 50% of the expected time for O(n) runtime
###################################################################

scaling_factor = 2
input_scaled = 'day5_twice.txt'
f1 = 'top_crates(f)'
f2 = 'top_crates(input_scaled)'

def get_variance(f1, f2, iter):
    input_time_n = timeit.timeit(f1, number=iter, globals=globals())
    input_time_n_scaled = timeit.timeit(f2, number=iter, globals=globals())
    input_time_n_expected = input_time_n_scaled / scaling_factor
    return abs((input_time_n / input_time_n_expected) - 1) 

variance = get_variance(f1, f2, 10)
result = "Yay!" if variance < 0.50 else "Boo!"
print(f'Variance is {variance:.2%} {result}')

