/*
	link: https://leetcode.com/problems/richest-customer-wealth/submissions/
	memory: O(1)
	time: O(n * m), row * column
	tag: Array, Matrix
*/
package main

import (
	"fmt"
)

func maximumWealth(accounts [][]int) int {
	 s := 0;

	for i := 0; i < len(accounts); i++ {
		t := 0
		for j := 0; j < len(accounts[i]); j++ {
			t += accounts[i][j]
		}

		if(t > s) {
			s = t;
		}
		
	}

	return s;
}

func main() {
	s := [][]int {
		{1, 2, 3},
		{10, 2, 1},
	}


	fmt.Println(maximumWealth(s)) 
}