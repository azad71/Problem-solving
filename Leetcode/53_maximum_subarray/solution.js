function findMaximumSubArray(nums) {
  let maxSum = nums[0];
  let runningSum = 0;

  for (let i = 0; i < nums.length; i++) {
    if (runningSum < 0) {
      runningSum = 0;
    }

    runningSum += nums[i];
    maxSum = Math.max(maxSum, runningSum);
  }

  return maxSum;
}

let arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4];

console.log(findMaximumSubArray(arr));
