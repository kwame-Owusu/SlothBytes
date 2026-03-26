package dailytemperatures

func dailyTemps(arr []int) []int {
	output := make([]int, len(arr))

	for i := range arr {
		for j := i + 1; j < len(arr); j++ {
			if arr[j] > arr[i] {
				output[i] = j - i
				break
			}
		}
	}

	return output
}
