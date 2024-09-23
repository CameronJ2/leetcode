class Solution {
  /**
   * @param {string} s
   * @param {string} t
   * @return {boolean}
   */
  isAnagram(s, t) {
    if (s.length != t.length) {
      return false
    }

    let mapS = new Map()
    let mapT = new Map()

    for (let i = 0; i < s.length; i++) {
      if (mapS.has(s[i])) {
        mapS.set(s[i], mapS.get(s[i]) + 1)
      }
      if (!mapS.has(s[i])) {
        mapS.set(s[i], 1)
      }
      if (mapT.has(t[i])) {
        mapT.set(t[i], mapT.get(t[i]) + 1)
      }
      if (!mapT.has(t[i])) {
        mapT.set(t[i], 1)
      }
    }

    for (let [key, value] of mapS) {
      if (mapT.get(key) !== value) {
        return false
      }
    }

    return true
  }
}

const solution = new Solution()

console.log(solution.isAnagram("hello", "ehllo"))
