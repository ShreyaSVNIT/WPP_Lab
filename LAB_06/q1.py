L = int(input())
R = int(input())
print((1 << (R.bit_length())) - 1 if L == 0 else (1 << ((L ^ R).bit_length())) - 1)