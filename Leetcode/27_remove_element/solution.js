function removeElement(nums, val) {
  let position = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      nums[position] = nums[i];
      position++;
    }
  }
  return position;
}

console.log(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2));
