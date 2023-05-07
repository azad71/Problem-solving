function createCounter(init) {
  let n = init;
  return {
    increment: () => (n += 1),
    reset: () => {
      n = init;
      return n;
    },
    decrement: () => (n -= 1),
  };
}

const counter = createCounter(5);
console.log(counter.increment()); // 6
console.log(counter.reset()); // 5
console.log(counter.decrement()); // 4
console.log(counter.decrement()); // 3
console.log(counter.increment()); // 4
console.log(counter.reset()); // 5
