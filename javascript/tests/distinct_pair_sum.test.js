const distinctPairSum = require('../distinct_pair_sum');

function sortArray(arr, k) {
  let res = distinctPairSum(arr, k);
  res = res.map(arr => arr.sort((a, b) => a - b));
  return JSON.stringify(res.sort((a, b) => a[0] - b[0]));
}

test('returns an empty array when there are no pairs that sum up to k', () => {
  expect(distinctPairSum([3, 4, 2, 1, 5, 2, 8, 2], 100).length).toBe(0);
  expect(distinctPairSum([], 100).length).toBe(0);
  expect(distinctPairSum([59], 100).length).toBe(0);
});

test('only returns distinct pairs', () => {
  expect(sortArray([0, 1, 1, 2, 0, 1, 1], 2)).toBe(JSON.stringify([[0, 2], [1, 1]]));
  expect(sortArray([3, 4, 2, 1, 5, 2, 8, 2], 10)).toBe(JSON.stringify([[2, 8]]));
  expect(sortArray([59, 41], 100)).toBe(JSON.stringify([[41, 59]]));
  expect(sortArray([1, 0, 0, 10, -10, 5, 4, 3, -3, -3], 0)).toBe(JSON.stringify([[-10, 10], [-3, 3], [0, 0]]));
});
