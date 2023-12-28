# Enter your code here. Read input from STDIN. Print output to STDOUT
from calendar import day_name, weekday

mon, day, yr = map(int, input().split())

print(day_name[weekday(int(yr),int(mon),int(day))].upper())