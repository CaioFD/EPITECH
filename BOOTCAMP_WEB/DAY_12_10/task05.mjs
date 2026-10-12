export function range(start, end, step) {
  if (step === undefined) {
    step = start < end ? 1 : -1;
  }

  const result = [];

  if (step > 0) {
    for (let i = start; i <= end; i += step) {
      result.push(i);
    }
  } else if (step < 0) {
    for (let i = start; i >= end; i += step) {
      result.push(i);
    }
  }

  return result;
}