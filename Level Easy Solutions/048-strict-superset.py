# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(map(int, input().split()))
set_count = int(input())

flag = True

for _ in range(set_count):
    sub_set = set(map(int, input().split()))

    if sub_set.difference(setA):
        flag = flag and False
print(flag)
