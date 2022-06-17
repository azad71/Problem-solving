function isPalindrome(s) {
  let start = 0;
  let end = s.length - 1;

  const isAlphaNum = (c) => (c >= 47 && c <= 57) || (c >= 97 && c <= 122) || (c >= 65 && c <= 90);

  while (start < end) {
    if (!isAlphaNum(s[start].charCodeAt())) {
      start++;
      continue;
    }

    if (!isAlphaNum(s[end].charCodeAt())) {
      end--;
      continue;
    }

    if (s[start].toLowerCase() !== s[end].toLowerCase()) {
      return false;
    }

    start++;
    end--;
  }

  return true;
}

console.log(isPalindrome("A man, a plan, a canal: Panama"));
console.log(isPalindrome("A man, a plan"));
console.log(isPalindrome(" "));
console.log(isPalindrome("race a car"));
console.log(isPalindrome("001}10)"));
