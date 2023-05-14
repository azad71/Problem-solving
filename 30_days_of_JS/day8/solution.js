// editorial: https://leetcode.com/problems/allow-one-function-call/editorial

function once(fn) {
  let isCalled = false;

  return function (...args) {
    if (!isCalled) {
      isCalled = true;
      return fn(...args);
    }
  };
}

const fn = (...args) => {
  let sum = 0;
  for (const arg of args) {
    sum += arg;
  }
  return sum;
};

const a = once(fn);

console.log(a(1, 2, 3)); // 6
console.log(a(1, 2, 3)); // undefined
console.log(a(1, 2, 3)); // undefined
