# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
earn = 0
size = list(map(int, input().split()))
n = int(input())
products = Counter(size)

for i in range(n):
    s_size, price = list(map(int, input().split()))
    if products[s_size]>0:
        earn += price
        products[s_size] -= 1

print(earn)