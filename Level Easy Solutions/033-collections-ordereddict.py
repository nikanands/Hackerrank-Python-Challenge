# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

inp = int(input())
items_list = [input().split() for i in range(inp)]
ordered_dict = OrderedDict()

for i in range(inp):
    item = items_list[i]
    item_name = ' '.join(item[:-1])
    price = int(item[-1])

    ordered_dict[item_name] = price * items_list.count(item)

for item in ordered_dict:
    print(f'{item} {ordered_dict[item]}')
