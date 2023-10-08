/**
 * @param {number[]} nums
 * @return {number}
 */
function majorityElement(nums) {
  let count1 = 0;
  let count2 = 0;
  let candidate1 = 0;
  let candidate2 = 0;

  for (let num of nums) {
    if (num === candidate1) {
      count1++;
    } else if (num === candidate2) {
      count2++;
    } else if (count1 === 0) {
      candidate1 = num;
      count1 = 1;
    } else if (count2 === 0) {
      candidate2 = num;
      count2 = 1;
    } else {
      count1--;
      count2--;
    }
  }

  count1 = 0;
  count2 = 0;

  for (let num of nums) {
    if (num === candidate1) count1++;
    else if (num === candidate2) count2++;
  }

  const result = new Set();
  const majority = parseInt(nums.length / 3);

  if (count1 > majority) result.add(candidate1);
  if (count2 > majority) result.add(candidate2);

  return [...result];
}

function majorityElementWithHashMap(nums) {
  let occurance = {};

  for (let num of nums) {
    if (occurance[num]) occurance[num]++;
    else occurance[num] = 1;
  }

  const majority = parseInt(nums.length / 3);
  const result = [];

  Object.entries(occurance).forEach(([key, value]) => {
    if (value > majority) result.push(+key);
  });

  return result;
}

console.log(majorityElement([3, 2, 1, 3, 2, 4, 4, 3, 4, 4, 3])); // [3, 4]
console.log(majorityElement([1, 2])); // [1, 2]
console.log(majorityElement([3, 2, 3])); // [3]
console.log(majorityElement([0, 0, 0])); // [0]
