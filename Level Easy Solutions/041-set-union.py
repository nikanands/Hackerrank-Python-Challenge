# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
N = set(map(int, input().split()))

b = int(input())
B = set(map(int, input().split()))

union = N.union(B)
print(len(union))