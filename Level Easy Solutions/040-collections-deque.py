# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

inp = int(input())
commands = [input() for _ in range(inp)]
nums = deque()

for command in commands:
    command = command.split()
    if command[0] == 'append':
        nums.append(command[1])
    elif command[0] == 'appendleft':
        nums.appendleft(command[1])
    elif command[0] == 'pop':
        nums.pop()
    elif command[0] == 'popleft':
        nums.popleft()

[print(num, end=' ') for num in nums]