class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        let res = [];
        let stack = [];
        const backTrack = (OpenB, ClosedB) => {
            if ( OpenB === n && ClosedB === n){
                let str = "";
                for (const i of stack){
                    str += i;
                }
                res.push(str);
                return;
            }
            if (OpenB < n){
                stack.push('(');
                backTrack(OpenB + 1, ClosedB);
                stack.pop();
            }
            if (ClosedB < OpenB){
                stack.push(')');
                backTrack(OpenB, ClosedB + 1);
                stack.pop();
            }
        }
        backTrack(0, 0);
        return res;
    }
}
