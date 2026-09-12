class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        };
        let stack = [];
        for( const b of  s){
            let isChar = b in map;

            if (!isChar){
                stack.push(b)
                continue
            }

            if (!stack || stack[stack.length - 1] != map[b]){
                return false
            }
            stack.pop()
        }

        return stack == 0
    }
}
