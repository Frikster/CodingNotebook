// lesson 7: Cover "Manhattan skyline" using the minimum number of rectangles.

function solution(H) {
    let heightStack = [H[0]];
    let res = 1;
    for (let i = 1; i < H.length; i++) {
        if (H[i] > heightStack[heightStack.length - 1]) {
            res += 1;
            heightStack.push(H[i]);
            continue;
        }
        while (heightStack.length > 0 && H[i] < heightStack[heightStack.length - 1]) {
            heightStack.pop();
        }
        if (heightStack[heightStack.length - 1] !== H[i]) {
            heightStack.push(H[i]);
            res += 1;
        }
    }
    return res;
}