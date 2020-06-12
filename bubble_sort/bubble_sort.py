def bubble_sort(arr: list):
    length_arr = len(arr)

    for i in range(length_arr):
        for j in range(length_arr-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


if __name__ == "__main__":
    arr = [5, 1, 8, 4, 9, 3, 6, 4, 8, 11, 15, 10, 7]
    print(bubble_sort(arr))
