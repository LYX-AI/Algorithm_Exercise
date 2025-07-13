public class MoveZeroes {
    public void moveZeroes(int[] nums){
        Integer n = nums.length;
        for(int i=0;i<n;i++){
            boolean sweep=false;
            for(int j=0;j<n-i-1;j++){
                if(nums[j]==0){
                    int temp=nums[j];
                    nums[j]=nums[j+1];
                    nums[j+1]=temp;
                    sweep=true;
                }
            }
            if(sweep==false){
                break;
            }
        }
    }
}
