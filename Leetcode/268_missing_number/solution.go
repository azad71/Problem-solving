package main

import "fmt"

func missingNumber(nums []uint32) uint32 {

	var s2 uint32 = 0;

	for _, value := range nums {
		s2 += value;
	}

	return (uint32)((len(nums) * (len(nums) + 1)) / 2) - s2;
}

func main() {
	nums := []uint32 {0}

	fmt.Println(nums);

	fmt.Println(missingNumber((nums)))
}