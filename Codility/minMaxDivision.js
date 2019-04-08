// Lesson 14: Divide array A into K blocks and minimize the largest sum of any block.
// Best explanation I could find: https://stackoverflow.com/a/42635035/2734863

function solution(K, M, A) {
    let lower = Math.max(...A);
    let upper = 0;
    A.forEach(el => upper += el);
    if (K >= A.length) return lower;
    if (K === 1) return upper;
    let smallestSum = 0;
    // Iterative = no large stack problems
    while(lower <= upper) {
        let mid = Math.floor((upper + lower) / 2);
        let blocks = blockCount(A, mid);
        if (blocks > K) {
            // i.e. bsearch(mid+1, upper)
            // Too many blocks, reduce by increasing mid = increasing max sum of block
            lower = mid + 1;
        } else if (blocks <= K) {
            // i.e. bsearch(lower, mid-1)
            // Number of blocks allowable, but need to continue checking with more blocks to find smallestSum
            // decrease mid = decrease max sum of block = add more blocks
            smallestSum = mid;
            upper = mid - 1;
        }
    }
    
    return smallestSum;
}

function blockCount(A, mid) {
    let blocks = 1;
    let blockSum = 0;
    A.forEach(el => {
        if (blockSum + el > mid) {
            blocks++;
            blockSum = el;
        } else {
            blockSum += el;
        }
    });
    return blocks
}


// Recursive - Stack overflow for very large input
// Not quite right - TODO: fix
function solution(K, M, A) {
    let lower = Math.max(...A);
    let upper = 0;
    A.forEach(el => upper += el);
    if (K >= A.length) return lower;
    if (K === 1) return upper;
    return bsearch(A, K, lower, upper)
}

function bsearch(A, K, lower, upper) {
    let mid = Math.floor((upper + lower) / 2);
    let blocks = 1;
    let blockSum = 0;
    let largeSum = 0;
    A.forEach(el => {
        if (blockSum + el > mid) {
            blocks++;
            if (blockSum > largeSum) largeSum = blockSum;
            blockSum = el;
        } else {
            blockSum += el;
        }
    });

    if (blocks === K) return largeSum;

    if (blocks < K) {
        return bsearch(A, K, lower, mid)
    } else {
        return bsearch(A, K, mid + 1, upper)
    }

}
