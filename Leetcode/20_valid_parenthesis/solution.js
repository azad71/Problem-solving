function isValid(s) {
  const p = [];

  const open = ["(", "[", "{"];
  const close = [")", "}", "]"];

  if (close.includes(s[0])) return false;

  for (let i = 0; i < s.length; i++) {
    if (open.includes(s[i])) {
      p.push(s[i]);
    } else {
      const lastValue = p.slice(-1)[0];
      if (
        (s[i] === ")" && lastValue === "(") ||
        (s[i] === "}" && lastValue === "{") ||
        (s[i] === "]" && lastValue === "[")
      ) {
        p.pop();
      } else {
        p.push(s[i]);
      }
    }
  }

  return p.length === 0;
}

console.log(isValid("()[]{}"));
console.log(isValid("[{()}]"));
console.log(isValid("(("));
console.log(isValid("([)]"));
console.log(isValid("])("));
console.log(isValid("(])"));
