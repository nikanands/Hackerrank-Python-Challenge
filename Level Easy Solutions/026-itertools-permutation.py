# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations
s,n = input().split()
output = list(permutations(s,int(n)))
perms = sorted([''.join(a) for a in output])
[print(perm.upper()) for perm in perms]
