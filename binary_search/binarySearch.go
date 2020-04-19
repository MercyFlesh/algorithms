package main

import "fmt"

func is_sort(slice []int) bool {
	for id, _ := range slice[:len(slice)-1] {
		if slice[id] > slice[id+1] {
			return false
		}
	}

	return true
}

func binarySearch(slice []int, find_key int) int {

	if is_sort(slice) {
		left := 0
		right := len(slice)

		for left <= right {
			mid := (left + right) / 2

			if mid > len(slice)-1 {
				break
			}

			switch {
			case slice[mid] == find_key:
				return mid
			case find_key < slice[mid]:
				right = mid - 1
			case find_key > slice[mid]:
				left = mid + 1
			}
		}
	}

	return -1
}

func main() {
	some_slice := []int{1, 2, 4, 5, 6, 7}
	fmt.Println(binarySearch(some_slice, 4))
}
