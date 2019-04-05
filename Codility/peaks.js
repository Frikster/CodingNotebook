// Lesson 10: Divide an array into the maximum number of same-sized blocks, each of which should contain an index P such that A[P - 1] < A[P] > A[P + 1].
// TODO: still has small bug? https://app.codility.com/demo/results/trainingDC4TTM-VDS/

function solution(A) {
    let closestPeakBelow = { 0: Infinity };
    for (let i = 1; i < A.length; i++) {
        // A[i+1] undefined and thus A[i] > A[i+1] false for i = A.length-1
        if (A[i] > A[i - 1] && A[i] > A[i + 1]) closestPeakBelow[i] = 0;
        else if (closestPeakBelow[i - 1] === Infinity) closestPeakBelow[i] = Infinity;
        else closestPeakBelow[i] = closestPeakBelow[i - 1] + 1;
    }
    let closestPeakAbove = {};
    closestPeakAbove[A.length - 1] = Infinity;
    for (let i = A.length - 2; i >= 0; i--) {
        if (A[i] > A[i - 1] && A[i] > A[i + 1]) closestPeakAbove[i] = 0;
        else if (closestPeakAbove[i + 1] === Infinity) closestPeakAbove[i] = Infinity;
        else closestPeakAbove[i] = closestPeakAbove[i + 1] + 1;
    }
    // console.log(closestPeakAbove);
    // console.log(closestPeakBelow);
    let res = 0;
    for (let blocks = 1; blocks < A.length; blocks++) {
        if (A.length % blocks !== 0) continue;
        let blockLen = A.length / blocks;
        let left = 0;
        let right = blockLen - 1;
        while (right < A.length) {
            if (!(closestPeakBelow[right] <= blockLen && closestPeakAbove[left] <= blockLen)) return res;
            // console.log(`${left} ${right}`)
            left += blockLen;
            right += blockLen;
        }
        // a peak exists for each block
        res = blocks;
        // console.log(res)
    }
    return res;
}