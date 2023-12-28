#Enter your code here. Read input from STDIN. Print output to STDOUT
import re
inp = int(input())
for _ in range(inp):
    try:
        print(bool(re.compile(input())))
    except:
        print('False')