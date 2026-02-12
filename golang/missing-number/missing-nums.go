package missingnumber

import "slices"

func missingNum(nums []int) int {
	nArr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

	for _, n := range nArr {
		if !slices.Contains(nums, n) {
			return n
		}
	}

	return -1
}
