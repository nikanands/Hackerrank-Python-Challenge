n = int(input())
nums = set(map(int, input().split()))
N = int(input())
instructions = [input() for _ in range(N)]

for inst in instructions:
    inst = inst.split()
    if inst[0] == "remove":
        nums.remove(int(inst[1]))
    elif inst[0] == "discard":
        nums.discard(int(inst[1]))
    elif inst[0] == "pop":
        nums.pop()

print(sum(nums))