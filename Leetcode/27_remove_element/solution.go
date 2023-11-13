package removeelement

func removeElement(nums []int, val int) int {
	postion := 0

	for idx, num := range nums {
		if num != val {
			nums[postion] = nums[idx]
			postion++
		}
	}

	return postion
}

func main() {
	nums := []int{0, 1, 2, 2, 3, 0, 4, 2}
	removeElement(nums, 2)
}
