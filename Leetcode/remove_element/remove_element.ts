// function removeElement(nums: number[], val: number): number {
//   let leftIdx = 0;
//   let rightIdx = nums.length - 1;

//   let currEmptySlot = Infinity;

//   while (leftIdx < rightIdx) {
//     console.log({ leftIdx, rightIdx, num: nums[leftIdx] });
//     if (nums[leftIdx] === val) {
//       currEmptySlot = leftIdx;
//       // console.log({ num: nums[leftIdx], currEmptySlot });
//     } else {
//       nums[currEmptySlot] = nums[leftIdx];
//       currEmptySlot += 1;
//     }

//     delete nums[leftIdx];

//     leftIdx += 1;
//   }

//   return currEmptySlot;
// }

function removeElement(nums: number[], val: number) {
  let k = 0;

  for (let i = 0; i < nums.length; i++) {
    console.log(i);
    // if (nums[i] !== val) {
    //   nums.unshift(nums[i]);
    //   k += 1;
    // }
  }

  console.log(nums);

  return k;
}

let a = [0, 1, 2, 2, 3, 0, 4, 2];

console.log(removeElement(a, 2));
