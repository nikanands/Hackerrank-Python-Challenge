def count_substring(string, sub_string):
    count = 0

    while sub_string in string:
        index = string.index(sub_string)
        count += 1
        string = string[index + 1:]
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)