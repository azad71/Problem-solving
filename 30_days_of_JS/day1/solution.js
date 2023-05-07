function helloWorld() {
  return function () {
    return "Hello World";
  };
}

const hello = helloWorld();

console.log(hello());
