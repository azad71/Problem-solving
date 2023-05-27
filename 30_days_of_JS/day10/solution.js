// https://leetcode.com/problems/curry/editorial

function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn(...args);
    }

    return (...nextArgs) => curried(...args, ...nextArgs);
  };
}

const sum = (a, b, c) => a + b + c;

const csum = curry(sum);
console.log(csum(1)(2)(3));
