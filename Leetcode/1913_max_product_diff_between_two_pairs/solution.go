package main

import (
	"fmt"
	"math"
	"sort"
)

func maxProductDifference1(nums []int) int {
	sort.Ints(nums[:])

	l := len(nums)

	return (nums[l-1] * nums[l-2]) - (nums[0] * nums[1])

}

func maxProductDifference2(nums []int) int {

	firstB := 0
	secondB := 0
	firstS := math.MaxInt16
	secondS := math.MaxInt16

	for _, num := range nums {
		if num < firstS {
			secondS = firstS
			firstS = num
		} else if num < secondS {
			secondS = num
		}

		if num > firstB {
			secondB = firstB
			firstB = num
		} else if num > secondB {
			secondB = num
		}
	}

	return (firstB * secondB) - (firstS * secondS)
}

func main() {
	nums := []int{5, 6, 2, 7, 4}
	res := maxProductDifference2(nums)

	fmt.Print(res)

	res = maxProductDifference1(nums)
	fmt.Print(res)

}
