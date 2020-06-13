package main

import (
	"fmt"
)

func bubbleSort(arr []int) []int {
	var length int = len(arr)

	if length > 1 {
		for i := range arr {
			for j := 0; j < length-i-1; j++ {
				if arr[j] > arr[j+1] {
					arr[j], arr[j+1] = arr[j+1], arr[j]
				}
			}
		}
	}

	return arr
}

func main() {
	fmt.Println(bubbleSort([]int{5, 1, 8, 4, 9, 3, 6, 4, 8, 11, 15, 10, 7}))
}
