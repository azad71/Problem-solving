// editorial: https://leetcode.com/problems/filter-elements-from-array/editorial/

function filter(arr, fn) {
  const newArr = new Array(arr.length);
  let loc = 0;

  for (let i = 0; i < arr.length; i++) {
    if (fn(arr[i], i)) {
      newArr[loc] = arr[i];
      loc++;
    }
  }

  while (newArr.length > loc) {
    newArr.pop();
  }

  return newArr;
}
