def is_sorted(arr: list):
    for i in range(arr)-1:
        if arr[i] > arr[i + 1]:
            return False
    return True


def binary_search(arr: list, find_key):
    if is_sorted:
        left = 0; right = len(arr)
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid > len(arr) - 1:
                break

            if find_key < arr[mid]:
                right = mid - 1
            elif find_key > arr[mid]:
                left = mid + 1
            else:
                return mid
            
            
    else:
        return -1

if __name__ == "__main__":
    some_list = [1, 2, 4, 5, 6]
    print(binary_search(some_list, 6))
