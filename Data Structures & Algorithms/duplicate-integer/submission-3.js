class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let tempList = [];
        for (const i of nums){
            if (tempList.includes(i)){
                return true;
            };
            tempList.push(i);
        };
        return false;
    };
};
