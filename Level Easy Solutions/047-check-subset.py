# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = int(input())

for t in range(inp):
    a_size = int(input())
    setA = set(map(int, input().split()))
    b_size = int(input())
    setB = set(map(int, input().split()))
    if setA.difference(setB):
        print(False)
    else:
        print(True)