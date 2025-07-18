import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n =nums.length;
        List<List<Integer>> result=new ArrayList<>();
        for(int i=0;i<n;i++){
            if(i>0||nums[i]==nums[i+1]){
                continue;
            }
            int left=i+1;
            int right=n-1;
            while (left<right){
                int total=nums[i]+nums[right]+nums[left];
                if(total==0){
                    List<Integer> subresult=new ArrayList<>();
                    subresult.add(nums[i]);
                    subresult.add(nums[right]);
                    subresult.add(nums[left]);
                    result.add(subresult);
                    while(left<right&&nums[left]==nums[left+1]){
                        left=left+1;
                    }
                    while(left<right&&nums[right]==nums[right-1]){
                        right=right-1;
                    }
                    left=left+1;
                    right=right-1;
                } else if (total>0) {
                    right-=1;
                }
                else {
                    left+=1;
                }
            }
        }
        return result;
    }

}
