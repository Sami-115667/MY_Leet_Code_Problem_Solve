/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    let x=nums.slice(0,n);
    let y=nums.slice(n);
    let ans=[]
    for(let i=0;i<n;i++){
        ans= ans.concat(x[i]);
         ans= ans.concat(y[i]);
    }
    return ans;
};