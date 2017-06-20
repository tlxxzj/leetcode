/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    candidates.sort();
    ret = [];
    function dfs(i, sum, l){
        if (sum == 0){
            ret.push(l.slice());
            return;
        }
        if (i <0 || sum < 0) return;
        low = i-1;
        while (low >=0  && candidates[low] == candidates[i]) low--;
        dfs(low, sum ,l);
        l.push(candidates[i]);
        dfs(i-1, sum-candidates[i], l);
        l.pop();
    }
    dfs(candidates.length-1, target, []);
    return ret;
};