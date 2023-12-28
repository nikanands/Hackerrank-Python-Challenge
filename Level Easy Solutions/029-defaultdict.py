# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = list(map(int, input().split()))
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

default_dict = defaultdict(lambda: '-1')

for a in set(A):
    default_dict[a] = ' '.join([str(i + 1) for i, x in enumerate(A) if x == a])

print(*(default_dict[b] for b in B), sep='\n')

