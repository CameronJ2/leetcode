// Solution does not work 100%. Time complexity is O(n), but space complexity is also O(n).
// See chatGPT solution for proper result

public class OptimizedSolution {
    public int[] productExceptSelf(int[] nums) {
        int[] productArray = new int[nums.length];
        int[] prefixArray = new int[nums.length];
        int[] postfixArray = new int[nums.length];
        int runningResult = 1;

        for (int i = 0; i < nums.length; i++) {
            prefixArray[i] = nums[i] * runningResult;
            runningResult = prefixArray[i];
        }

        runningResult = 1;

        for (int i = nums.length - 1; i >= 0; i--) {
            postfixArray[i] = nums[i] * runningResult;
            runningResult = postfixArray[i];
        }

        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                productArray[i] = postfixArray[i + 1];
            } else if (i == nums.length - 1) {
                productArray[i] = prefixArray[i - 1];
            } else {
                productArray[i] = prefixArray[i - 1] * postfixArray[i + 1];
            }
        }

        return productArray;
    }
}
