# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
divisor = int(input())

res = (divmod(num, divisor))

print(res[0], res[1], res, sep='\n')
