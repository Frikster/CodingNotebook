// Lesson 12: There are N chocolates in a circle. Count the number of chocolates you will eat.

// O(log(a + b)) - Greatest Common Denominator
// a > b
function gcd(a, b) {
    if (a % b === 0) return b;
    return gcd(b, a % b)
}

// Least Common Multiple
function lcm(a, b) {
    return (a * b) / gcd(a, b);
}

function solution(N, M) {
    return lcm(N, M) / M;
}