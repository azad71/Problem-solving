// Link -> https://leetcode.com/problems/longest-common-prefix/

var longestCommonPrefix = function (strs) {
  let first = strs[0];
  let result = "";

  for (let i = 0; i < first.length; i++) {
    let isMatch = true;

    for (let j = 1; j < strs.length; j++) {
      if (first[i] !== strs[j][i]) {
        isMatch = false;
        break;
      }
    }

    if (isMatch) result += first[i];
    else break;
  }

  return result;
};
