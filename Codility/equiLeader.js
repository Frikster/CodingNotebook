// Lesson 8: Find the number of indexes S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.

function solution(A) {
  let counter = {};
  let leader = null;
  for (let i = 0; i < A.length; i++) {
    A[i] in counter ? counter[A[i]]++ : (counter[A[i]] = 1);
    if (counter[A[i]] > A.length / 2) leader = A[i];
  }
  if (leader === null) return 0;
  let leftLeaderCount = 0;
  let rightLeaderCount = counter[leader];
  let res = 0;
  for (let i = 0; i < A.length; i++) {
    if (A[i] === leader) {
      leftLeaderCount++;
      rightLeaderCount--;
    }
    if (
      leftLeaderCount > (i + 1) / 2 &&
      rightLeaderCount > (A.length - i - 1) / 2
    )
      res += 1;
  }
  return res;
}