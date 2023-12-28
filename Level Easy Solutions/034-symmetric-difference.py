a = int(input())
A = set(map(int, input().split()))

b = int(input())
B = set(map(int, input().split()))

union = A.union(B)
common = A.intersection(B)
results = sorted((A.union(B)).difference(A.intersection(B)))

for i in results:
    print(i)
