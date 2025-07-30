import java.lang.Math;
public class MaximumSubarray {
    public int maxSubArray(int[] nums) {
        int CurrentSum= nums[0];
        int Current_result=nums[0];

        for (int i=1;i<nums.length;i++){
            CurrentSum=Math.max(CurrentSum+nums[i],nums[i]);
            Current_result=Math.max(CurrentSum,Current_result);
        }
        return Current_result;
    }

    public static void main(String args[]){
        MaximumSubarray sol= new MaximumSubarray();
        int[] nums= {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println(sol.maxSubArray(nums));
    }
}
