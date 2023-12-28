# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

inp, num = input().split()

for i in range(int(num), int(num) + 1):
    combos = (list(combinations_with_replacement(inp, i)))

    results = sorted([''.join(sorted(n)) for n in combos])

    for result in results:
        print(result)