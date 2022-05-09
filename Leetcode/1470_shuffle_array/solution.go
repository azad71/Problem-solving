/*
	link: https://leetcode.com/problems/shuffle-the-array/
	space: O(n)
	time: O(n)
	tag: Array
*/

package main

import "fmt"

func shuffleArray(nums []int, n int) []int {
	shuffled := make([]int, 2*n);


	for i := 0; i < n; i++ {
		shuffled[i*2] = nums[i];
		shuffled[i*2+1] = nums[i+n];
	}

	return shuffled;
}

func main() {
	nums := []int {2,5,1,3,4,7};

	fmt.Println(nums)

	fmt.Println(shuffleArray(nums, len(nums)/2))
}