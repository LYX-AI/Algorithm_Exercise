package List;

public class MinimumSizeSubarraySum {
    public int minSubArrayLen(int target, int[] nums) {
        int i = 0;
        int sum = 0;
        int result = Integer.MAX_VALUE ;
        for (int j=0;j<nums.length;j++){
            sum+=nums[j];
            while(sum>=target){
                result=Math.min(result, j-i+1);
                sum-=nums[i];
                i++;
            }
        }
          return result;
    }
    public static void  main(String[] args){
        int target = 7;
        int[] nums = {2,3,1,2,4,3};
        MinimumSizeSubarraySum solution =new MinimumSizeSubarraySum();
        System.out.println(solution.minSubArrayLen(target, nums));
}
}
