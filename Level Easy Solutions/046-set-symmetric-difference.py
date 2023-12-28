# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
N = set(map(int, input().split()))

b = int(input())
B = set(map(int, input().split()))

diff = N.symmetric_difference(B)
print(len(diff))