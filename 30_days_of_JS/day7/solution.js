// editorial: https://leetcode.com/problems/function-composition/editorial/

var compose = function (functions) {
  return function (x) {
    for (let i = functions.length - 1; i >= 0; i--) {
      x = functions[i].call(this, x); // to preserve the 'this' of parent function
    }
    return x;
  };
};

compose([(x) => x + 1, (x) => x * x, (x) => 2 * x])(4);
compose([(x) => 10 * x, (x) => 10 * x, (x) => 10 * x])(1);
compose([])(42);
