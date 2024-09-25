public class App {
    public static void main(String[] args) throws Exception {
        // LogNSolution Solution = new LogNSolution();
        GPTSolution Solution = new GPTSolution();

        int[] nums = { 1, 3, 5, 6 };
        int target = 2;

        int result = Solution.searchInsert(nums, target);
        System.out.println(result);

    }

}
