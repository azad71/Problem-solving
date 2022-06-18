function isAnagram(s, t) {
  if (s.length !== t.length) return false;

  let alphabets = new Array(26).fill(0);

  for (let i = 0; i < s.length; i++) {
    alphabets[s[i].charCodeAt() - 97]++;
    alphabets[t[i].charCodeAt() - 97]--;
  }

  for (let i = 0; i < alphabets.length; i++) {
    if (alphabets[i] !== 0) return false;
  }

  return true;
}

console.log(isAnagram("anagram", "nagaram"));
// console.log(isAnagram("anagram", "nagarmm"));
// console.log(isAnagram("ac", "bb"));
// console.log(isAnagram("a", "b"));
// console.log(isAnagram("a", "a"));
// console.log(isAnagram("aa", "ab"));
// console.log(isAnagram("rat", "car"));
