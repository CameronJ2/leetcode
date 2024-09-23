/* 
 * Very annoying problem. Kept getting an integer overflow
 * because I was checking if how mid * mid compares to 
 * x in the if conditions, when I was supposed to just 
 * divide x by mid instead.
 */

public class App {

    public static int mySqrt(int x) {
        int previous = 0;
        for (int i = 1; i <= x; i++) {
            int result = i * i;
            if (result == x) {
                return i;
            } else if (result > x) {
                return previous;
            }
            previous = i;
        }
        return previous;
    }

    public static int optimalSqrt(int x) {
        if (x == 0 || x == 1) {
            return x; // handle 0 and 1 explicitly
        }

        int left = 1;
        int right = x;
        int result = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (mid > x / mid) {
                right = mid - 1;
            } else {
                left = mid + 1;
                result = mid;
            }
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(optimalSqrt(2147395599));
    }
}
