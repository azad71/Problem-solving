package main

func solution(nums []int) []int {
	temp := 1

	output := make([]int, len(nums))

	// initialize output array with value 1
	for i := range output {
		output[i] = temp
	}

	for i := range nums {
		output[i] = temp
		temp *= nums[i]
	}

	temp = 1

	for i := len(output) - 1; i >= 0; i-- {
		output[i] *= temp
		temp *= nums[i]
	}

	return output
}

func main() {
	var nums = []int {1,2,3,4}
	solution(nums)
}

