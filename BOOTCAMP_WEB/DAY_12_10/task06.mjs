export function arrayFiltering(array, test) {
  const result = [];

  for (const value of array) {
    if (test(value)) {
      result.push(value);
    }
  }

  return result;
}