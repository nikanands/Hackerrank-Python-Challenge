# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

inp = int(input())

cols = input().split()
stu = namedtuple("Student", cols)
total = 0

for _ in range(inp):
    values = input().split()
    student = stu(*values)
    total += int(student.MARKS)

average = total / inp
print(format(average, ".2f"))