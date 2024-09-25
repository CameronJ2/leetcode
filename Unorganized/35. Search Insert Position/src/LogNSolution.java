public class LogNSolution {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        boolean earlyExit = false;

        while (!earlyExit) {
            if (nums[right] < target) {
                return nums.length;
            } else if (nums[left] > target) {
                return 0;
            }
            earlyExit = !earlyExit;
        }

        if (nums.length == 1) {
            if (target < nums[0]) {
                return 1;
            } else {
                return 0;
            }
        }

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[left] == target) {
                return left;
            } else if (nums[right] == target) {
                return right;
            } else if (nums[mid] == target) {
                return mid;
            } else if (right == left + 1) {
                if (nums[left] > target) {
                    return left;
                } else {
                    return right;
                }
            } else if (nums[mid] < target) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return -1;
    }

}
