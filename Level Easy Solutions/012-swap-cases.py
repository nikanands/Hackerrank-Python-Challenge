def swap_case(s):
    mod_s = []
    for i in s:
        if i == i.lower():
            mod_s.append(i.upper())
        else:
            mod_s.append(i.lower())
    return ''.join(mod_s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)