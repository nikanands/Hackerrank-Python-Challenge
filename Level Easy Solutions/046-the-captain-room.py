# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
inp = int(input())
num = list(map(int, input().split()))

result = [x for x, count in Counter(num).items() if count == 1]
print(*result)
