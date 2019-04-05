// Lesson 10: Find the minimal perimeter of any rectangle whose area equals N.

function solution(N) {
    let res = Infinity;
    Array.from({ length: Math.sqrt(N) }, (x, i) => i + 1).forEach(i => {
        if (N % i === 0) {
            let perimeter = Math.min(res, 2 * (i + (N / i)));
            if (perimeter < res) res = perimeter;
        }
    });
    return res;
}