# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

h = 'H' * n
space = ' ' * n
b_line = h + (space * 3) + h
c_line = (h * 5)

# top triangle
for i in range(1, n * 2 + 1, 2):
    print(("H" * i).center(2 * n - 1, ' '))

# top body
for _ in range(n + 1):
    print(b_line.center(n * 6 - 1, ' '))

# middle band
for _ in range(n // 2 + 1):
    print(c_line.center(n * 6 - 1, ' '))

# bottom body
for _ in range(n + 1):
    print(b_line.center(n * 6 - 1, ' '))

# bottom triangle
for i in range(n * 2 - 1, 0, -2):
    print(("H" * i).center(n * 10, ' '))
