# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = map(int, input().split())
b = map(int, input().split())

c = list(product(a,b))
[print(i, end=' ') for i in c]
