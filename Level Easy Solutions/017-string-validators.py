if __name__ == '__main__':
    s = input()

    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False

    for i in s:
        alnum = alnum or i.isalnum()
        alpha = alpha or i.isalpha()
        digit = digit or i.isdigit()
        lower = lower or i.islower()
        upper = upper or i.isupper()

    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
