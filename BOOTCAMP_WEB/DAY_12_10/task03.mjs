export function countGs(str) {
  let count = 0;
  for (const char of str) {
    if (char === "G" || char === "g") {
      count++;
    }
  }
  return count;
}