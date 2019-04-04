// Lesson 9: Find the maximal sum of any double slice.

function solution(A) {
    let maxEndingHere = { 0: 0 };
    let currSlice = 0;
    for (let i = 1; i < A.length - 1; i++) {
        currSlice = Math.max(currSlice + A[i], 0);
        maxEndingHere[i] = currSlice;
    }
    let maxStartingHere = {};
    maxStartingHere[A.length - 1] = 0;
    currSlice = 0;
    for (let i = A.length - 2; i >= 1; i--) {
        currSlice = Math.max(currSlice + A[i], 0);
        maxStartingHere[i] = currSlice;
    }
    let res = 0;
    for (let i = 0; i < A.length - 2; i++) {
        res = Math.max(res, maxEndingHere[i] + maxStartingHere[i + 2])
    }
    return res;
}