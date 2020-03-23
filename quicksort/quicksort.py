def partition(arr: list, left, right):
    l = left
    r = right

    pivot = arr[l]
    while l <= r:
        while arr[l] < pivot:
            l += 1
        
        while arr[r] > pivot:
            r -= 1
        
        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    return l


def quicksort(arr: list, left, right):
    if left < right:
        div = partition(arr, left, right)
        quicksort(arr, left, div - 1)
        quicksort(arr, div, right)


if __name__ == "__main__":
    arr = [5, 1, 8, 4, 9, 3, 6, 4, 8, 11, 15, 10, 7]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)