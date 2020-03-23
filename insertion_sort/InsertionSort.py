def InsertionSort(arr: list):
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        while arr[j] > temp and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1            
        arr[j + 1] = temp

    return arr


if __name__ == "__main__":
    arr = [5, 1, 8, 4, 9, 3, 6, 4, 8, 11, 15, 10, 7]
    print(InsertionSort(arr))