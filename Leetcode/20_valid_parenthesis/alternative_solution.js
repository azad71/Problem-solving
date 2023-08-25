function isValid(s) {
  let p = [];

  let pair = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  for (let el of s) {
    if (Object.keys(pair).includes(el)) p.push(el);
    else if (pair[p.slice(-1)[0]] === el) p.pop();
    else return false;
  }

  return p.length === 0;
}

console.log(isValid("()[]{}")); // true
console.log(isValid("[{()}]")); // true
console.log(isValid("((")); // false
console.log(isValid("([)]")); // false
console.log(isValid("])(")); // false
console.log(isValid("(])")); // false
