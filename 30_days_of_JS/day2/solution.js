function createCounter(n) {
  let counter = 0;
  return () => (counter++ > 0 ? n + counter - 1 : n);
}

// const counter = createCounter(10);
// console.log(counter()); // 10
// console.log(counter()); // 11
// console.log(counter()); // 12
// console.log(counter()); // 13
// console.log(counter()); // 13

// function createCounter(n) {
//   // your code here
// }

// const counter = createCounter(10);
// console.log(counter()); // 10
// console.log(counter()); // 11
// console.log(counter()); // 12
// console.log(counter()); // 13
// console.log(counter()); // 14

const sum = (function sum(a, b) {
  return a + b;
})(3, 2);

console.log(sum);
