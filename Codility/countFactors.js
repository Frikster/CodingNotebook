// Lesson 10: Count factors of given number n.

function solution(N) {
    let res = 0;
    Array.from({ length: Math.sqrt(N) }, (x, i) => i + 1).forEach(i => {
        if (i * i === N) res += 1;
        else if (N % i === 0) res += 2;
    });
    return res;
}