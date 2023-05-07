function createCounter(n) {
  let counter = 0;
  return () => (counter++ > 0 ? n + counter - 1 : n);
}

const counter = createCounter(-2);
console.log(counter()); // 10
console.log(counter()); // 11
console.log(counter()); // 12
console.log(counter()); // 13
console.log(counter()); // 13
