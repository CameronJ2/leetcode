class Solution {
  /**
   * @param {number[]} nums
   * @param {number} k
   * @return {number[]}
   */
  topKFrequent(nums, k) {
    let freqMap = new Map()
    let returnArray = []
    let sortedCount = []

    for (let i = 0; i <= nums.length; i++) {
      sortedCount.push([])
    }

    for (let i = 0; i < nums.length; i++) {
      if (freqMap.has(nums[i])) {
        freqMap.set(nums[i], freqMap.get(nums[i]) + 1)
      } else {
        freqMap.set(nums[i], 1)
      }
    }

    for (let [key, value] of freqMap) {
      sortedCount[value].push(key)
    }

    for (let i = sortedCount.length - 1; i >= 0; i--) {
      for (let j = 0; j < sortedCount[i].length; j++) {
        returnArray.push(sortedCount[i][j])
        if (returnArray.length === k) {
          return returnArray
        }
      }
    }
  }
}

const solution = new Solution()
console.log(solution.topKFrequent([1, 2, 2, 3, 3, 3], 2))
