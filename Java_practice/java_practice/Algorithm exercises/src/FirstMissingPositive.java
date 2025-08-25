public class FirstMissingPositive {
    public int firstMissingPositive(int[] nums) {
            int n = nums.length;
            for (int i=0;i<n;i++){
                while(nums[i]>=1&&nums[i]<n&&nums[nums[i]-1]!=nums[i]){
                    int index=nums[i]-1;
                    int temp=nums[index];
                    nums[index]=nums[i];
                    nums[i]=temp;

                }
            }
            for (int j=0;j<n;j++){
                if(nums[j]!=j+1){
                    return j+1;
                }
            }
            return n+1;
    }

    public static void main(String[] args){
        FirstMissingPositive solution= new FirstMissingPositive();
        int [] nums= {3, 4, -1, 1};
        System.out.println(solution.firstMissingPositive(nums));
    }
}
