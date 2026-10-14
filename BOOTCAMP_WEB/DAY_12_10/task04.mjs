export function fizzBuzz(num) {
  const terms = [];

  for (let i = 1; i <= num; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      terms.push("FizzBuzz");
    } else if (i % 3 === 0) {
      terms.push("Fizz");
    } else if (i % 5 === 0) {
      terms.push("Buzz");
    } else {
      terms.push(i);
    }
  }

  console.log(terms.join(", "));
}