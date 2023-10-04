/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

// with bubble sort
function mergeSortedArray(nums1, m, nums2, n) {
  if (n === 0) return nums1;

  for (let i = m, j = 0; i < m + n && j < n; i++, j++) {
    nums1[i] = nums2[j];
  }

  const len = m + n - 1;

  for (let i = 0; i < len; i++) {
    let swapped = false;
    for (let j = 0; j < len - i; j++) {
      if (nums1[j] > nums1[j + 1]) {
        let temp = nums1[j];
        nums1[j] = nums1[j + 1];
        nums1[j + 1] = temp;
        swapped = true;
      }
    }

    if (!swapped) break;
  }

   nums1.sort((a, b) = a - b)
}

function mergeSortedArrayWithInBuiltSort(nums1, m, nums2, n) {
  if (n === 0) return nums1;

     for (let i = m, j = 0; i < m + n && j < n; i++, j++) {
        nums1[i] = nums2[j];
    }

    nums1.sort((a, b) => a - b);
}

// with two pointer approach
function mergeSortedArrayWithTwoPointer(nums1, m, nums2, n) {
  if (n === 0) return nums1;

  let i = m - 1;
  let j = n - 1;
  let k = m + n - 1;

  while (j >= 0) {
    if (i >= 0 && nums1[i] > nums2[j]) {
      nums1[k] = nums1[i];
      i--;
    } else {
      nums1[k] = nums2[j];

      j--;
    }
    k--;
  }
}


console.log(mergeSortedArray([1, 2, 5, 7, 0, 0, 0, 0], 4, [1, 2, 3, 4], 4));
