public class GPTSolution {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2; // Calculate the middle index

            if (nums[mid] == target) {
                return mid; // Target found at the middle index
            } else if (nums[mid] < target) {
                left = mid + 1; // Move the left boundary to narrow the search
            } else {
                right = mid - 1; // Move the right boundary to narrow the search
            }
        }

        // At this point, left is the correct insertion position if the target is not
        // found
        return left;
    }
}
