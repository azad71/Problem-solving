function isPalindrome(s) {
  let n = [];
  for (let i = 0; i < s.length; i++) {
    let value = s[i].charCodeAt();
    if ((value >= 47 && value <= 57) || (value >= 97 && value <= 122)) {
      n.push(s[i]);
    } else if (value >= 65 && value <= 90) {
      n.push(s[i].toLowerCase());
    }
  }

  let start = 0;
  let end = n.length - 1;

  while (start < end) {
    if (n[start] !== n[end]) {
      return false;
    }
    start++;
    end--;
  }

  return true;
}

// console.log(isPalindrome("A man, a plan, a canal: Panama"));
// console.log(isPalindrome("A man, a plan"));
// console.log(isPalindrome(" "));
// console.log(isPalindrome("race a car"));
console.log(isPalindrome("001}10)"));
