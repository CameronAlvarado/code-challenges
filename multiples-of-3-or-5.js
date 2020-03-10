function solution(number) {
  // make a list of every number that increments up to given number
  const nums = [];
  for (i = 0; i < number; i++) {
    nums.push(i);
  }
  // declare array of new nums
  const newNums = [];
  // for each number...
  nums.forEach(num => {
    // check if number can floor to 3
    // if so add to new list of numbers
    num % 3 === 0 ? newNums.push(num) : undefined;
    // check if number can floor to 5
    // if number already in new list, move on to next number
    num % 5 === 0 && newNums.includes(num) === false
      ? newNums.push(num)
      : undefined;
  });
  // decalre a sum
  let sum = 0;
  // for each number in new number list, add together.
  newNums.forEach(num => (sum += num));
  // return sum.
  return sum;
}

const x = solution(10);
console.log(x);
