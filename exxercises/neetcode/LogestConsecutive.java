import java.util.HashSet;
import java.util.Set;

public class LogestConsecutive {

    public static void main(String[] args) {
        int[] input = new int[] { 2,20,4,10,3,4,5};

        int expectOutput =4;
        int result = longestConsecutive(input);
        if (result == expectOutput) {
            System.out.println("Success");
        } else {
            System.out.println("Failed");
        }
    }
    public static int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        
        int longest = 0;
        for (int i = 0; i < nums.length; i++) {
            if(!set.contains(nums[i] - 1)){
                int length = 0;
                while (set.contains(nums[i] + length)) {
                    length += 1;
                }
                longest = Math.max(length, longest);
            }
        }
        return longest;
    }

}