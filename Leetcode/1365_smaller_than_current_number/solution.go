package main

import "fmt"

func smallerThanCurrentNumber(nums []int) []int {

	result := make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		count := 0;
		for j := 0; j < len(nums); j++ {
			if nums[j] < nums[i] {
				count++;
			}
		}
		result[i] = count;
	}

	return result;

}

func main() {
	nums := []int {7,7,7,7};

	fmt.Println(smallerThanCurrentNumber((nums)))
}