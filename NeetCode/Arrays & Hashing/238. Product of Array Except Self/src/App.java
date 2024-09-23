public class App {
    public static void main(String[] args) throws Exception {
        // Solution Solution = new Solution();
        // OptimizedSolution OptimizedSolution = new OptimizedSolution();
        GPTSolution GPTSolution = new GPTSolution();

        int[] nums = { 1, 2, 3, 4 };

        // int[] result = Solution.productExceptSelf(nums);
        int[] result = GPTSolution.productExceptSelf(nums);

        for (int i = 0; i < result.length; i++) {
            System.out.println(result[i]);
        }

    }

}