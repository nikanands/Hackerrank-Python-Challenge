if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

sorted_unique_values = sorted(set(arr))
print(sorted_unique_values[-2])