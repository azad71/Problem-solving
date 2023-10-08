function mostFrequentEven(nums) {
  let evenOccurence = new Map();

  for (let num of nums) {
    if (num % 2 !== 0) continue;

    if (evenOccurence[num]) evenOccurence[num]++;
    else evenOccurence[num] = 1;
  }

  let maxEvenKey = -1;
  let maxEvenVal = -1;

  Object.entries(evenOccurence).forEach(([key, value]) => {
    if (value > maxEvenVal) {
      maxEvenVal = value;
      maxEvenKey = key;
    }
  });

  return maxEvenKey;
}

console.log(
  mostFrequentEven([
    6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 4, 4, 2, 3, 4, 1, 1, 4, 2, 2,
    2, 6, 6, 6,
  ])
);

console.log(mostFrequentEven([29, 47, 21, 41, 13, 37, 25, 7]));
