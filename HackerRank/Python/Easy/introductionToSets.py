def average(array):
    return sum(list(set(array)))/len(list(set(array)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)