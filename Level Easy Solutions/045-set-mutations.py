# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
setA = set(map(int, input().split()))
count = int(input())
for command in range(count):
    command = input().split()
    setB = set(map(int, input().split()))

    if command[0] == 'update':
        setA.update(setB)
    elif command[0] == 'intersection_update':
        setA.intersection_update(setB)
    elif command[0] == 'difference_update':
        setA.difference_update(setB)
    elif command[0] == 'symmetric_difference_update':
        setA.symmetric_difference_update(setB)
print(sum(setA))
