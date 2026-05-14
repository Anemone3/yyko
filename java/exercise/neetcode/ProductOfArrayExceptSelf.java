import java.util.Arrays;

public class ProductOfArrayExceptSelf {

    public static void main(String[] args) {
        int[] input = new int[] { 1, 2, 4, 6 };

        int[] expectOutput = new int[] { 48, 24, 12, 8 };
        int[] result = productExceptSelf(input);
        if (Arrays.equals(result, expectOutput)) {
            System.out.println("Success");
        } else {
            System.out.println("Failed");
        }
    }

    public static int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int postFix = 1;
        res[0] = 1;

        for (int i = 1; i < n; i++) {
            res[i] = nums[i - 1] * res[i - 1];
        }
        System.out.println(Arrays.toString(res));
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= postFix;
            postFix *= nums[i];
        }
        return res;
    }

    // public static int[] productExceptSelf(int[] nums) {
    // int n = nums.length;
    // int[] res = new int[n];
    // int[] pref = new int[n];
    // int[] suff = new int[n];
    // pref[0] = 1;
    // suff[n - 1] = 1;
    // for (int i = 1; i < n; i++) {
    // int num_val = nums[i - 1];
    // int num_pref = pref[i - 1];
    // System.out.println("indice: " + i);
    // System.out.println("num val -> " + num_val);
    // System.out.println("num val -> " + num_pref);
    // int result = nums[i - 1] * pref[i - 1];
    // System.out.println("result -> -> " + result);
    // pref[i] = result;
    // System.out.println(Arrays.toString(pref));
    // }

    // for (int i = n - 2; i >= 0; i--) {
    // suff[i] = nums[i + 1] * suff[i + 1];
    // }
    // System.out.println("elements suff" + Arrays.toString(suff));

    // for (int i = 0; i < n; i++) {
    // System.out.println("elements res" + Arrays.toString(res));

    // res[i] = pref[i] * suff[i];
    // }

    // System.out.println("elements preff" + Arrays.toString(pref));
    // System.out.println("elements suff" + Arrays.toString(suff));
    // return res;
    // }
}