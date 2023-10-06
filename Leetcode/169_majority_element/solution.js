/**
 * @param {number[]} nums
 * @return {number}
 */

// hash map approach, T = O(n), S = O(n)
function majorityElement(nums) {
  const occurance = {};

  for (let num of nums) {
    if (occurance[num]) occurance[num]++;
    else occurance[num] = 1;
  }

  let maxValue = -Infinity;
  let maxOccurence;

  Object.entries(occurance).forEach(([key, value]) => {
    if (value > maxValue) {
      maxValue = value;
      maxOccurence = key;
    }
  });

  return maxOccurence;
}

// applying Boyer-Moore Majority Voting Algorithm
// T = O(n), S = O(1)
function majorityElementWithMooreAlgorithm(nums) {
  let count = 0;
  let candidate = nums[0];

  for (let num of nums) {
    if (count === 0) {
      candidate = num;
      count++;
    } else if (num === candidate) {
      count++;
    } else if (num !== candidate) {
      count--;
    }
  }

  return candidate;
}

console.log(majorityElement([2, 2, 1, 1, 1, 2, 2]));
