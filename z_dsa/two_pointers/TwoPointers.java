import java.util.Arrays;

public class TwoPointers {

	public static void main(String[] args) {
		/* Leetcode 977. Squares of a Sorted Array */
		int[] input_nums = new int[] { -4, -1, 0, 3, 10 };
		// Output: [0,1,9,16,100]
		int[] result = sortedSquares(input_nums);
		System.out.println("Result: ");
		System.out.println(Arrays.toString(result));
	}

	/* Two pointer de extremo a extremo, left = 0 <-> right = max_length - 1 */
	public static int[] sortedSquares(int[] nums) {
		int left = 0;
		int right = nums.length - 1;
		int[] result = new int[nums.length];
		int index = nums.length - 1;
		while (left <= right) {
			int start = Math.abs(nums[left]);
			int last = Math.abs(nums[right]);
			if (start > last) {
				/* 
					resut[index] = nums[left] * nums[left];
					index--;
					es lo mismo que result[index--]
				*/
				result[index--] = nums[left] * nums[left];
				left++;
			} else {
				result[index--] = nums[right] * nums[right];
				right--;
			}
		}
		return result;
	}

}
