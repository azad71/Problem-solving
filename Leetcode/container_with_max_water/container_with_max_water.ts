/*
Link -> https://leetcode.com/problems/container-with-most-water/
Tag -> Array
*/

function maxArea(heights: number[]) {
  let maxWater = 0;
  let rightIdx = heights.length - 1;
  let leftIdx = 0;

  while (leftIdx !== rightIdx || leftIdx > rightIdx) {
    let moved = false;

    let area =
      (rightIdx - leftIdx) *
      (heights[leftIdx] < heights[rightIdx]
        ? heights[leftIdx]
        : heights[rightIdx]);

    maxWater = area > maxWater ? area : maxWater;

    if (heights[leftIdx] <= heights[rightIdx]) {
      leftIdx += 1;
      moved = true;
    } else if (heights[leftIdx] > heights[rightIdx]) {
      rightIdx -= 1;
      moved = true;
    }

    if (!moved) {
      break;
    }
  }

  return maxWater;
}
