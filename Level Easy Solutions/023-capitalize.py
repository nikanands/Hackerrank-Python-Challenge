def solve(s):
    words = s.split(' ')
    result = ''
    for word in words:
        result += word.capitalize() + ' '
    return result