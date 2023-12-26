# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

n = int(n)
m = int(m)
x = 1
for i in range(int(n / 2) + 1):
    if i == int(n / 2):
        print('-' * int((m - 7) / 2) + 'WELCOME' + '-' * int((m - 7) / 2))

    else:
        d = m - 3 * x
        print(int(d / 2) * '-' + x * '.|.' + int(d / 2) * '-')
        x += 2

x = x - 2

for i in range(int(n / 2), 0, -1):
    d = m - 3 * x
    print(int(d / 2) * '-' + x * '.|.' + int(d / 2) * '-')
    x -= 2
