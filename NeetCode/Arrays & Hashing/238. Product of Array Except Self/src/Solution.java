class Solution {
    public int[] productExceptSelf(int[] nums) {
        int runningProduct;
        int[] productArray = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            runningProduct = 1;

            for (int j = 0; j < nums.length; j++) {
                if (i == j) {
                    continue;
                }
                runningProduct *= nums[j];
            }

            productArray[i] = runningProduct;
        }

        return productArray;
    }
}