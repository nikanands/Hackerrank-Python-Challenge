# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

inp, num = input().split()

for i in range(1, int(num) + 1):
    combos = (list(combinations(inp, i)))

    results = sorted([''.join(sorted(n)) for n in combos])

    for result in results:
        print(result)

