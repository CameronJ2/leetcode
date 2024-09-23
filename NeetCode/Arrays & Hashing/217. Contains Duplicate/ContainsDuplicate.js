class Solution {
  /**
   * @param {number[]} nums
   * @return {boolean}
   */
  hasDuplicate(nums) {
    let usedNumbers = new Set()
    for (let i = 0; i < nums.length; i++) {
      if (usedNumbers.has(nums[i])) {
        return true
      }
      usedNumbers.add(nums[i])
      console.log(usedNumbers)
    }
    return false
  }
}

const solution = new Solution()

console.log(solution.hasDuplicate([1, 2, 3, 4, 2]))
