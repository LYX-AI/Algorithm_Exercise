import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SubarraySumEqualsK {
    public int subarraySum(int[] nums, int k) {
        Map<Integer,Integer> prefix_count=new HashMap<>();
        prefix_count.put(0,1);
        int prefix_sum=0;
        int result=0;
         for (int num:nums){
             prefix_sum+=num;
             result+=prefix_count.getOrDefault(prefix_sum-k,0);
             prefix_count.put(prefix_sum,prefix_count.getOrDefault(prefix_sum,0)+1);
         }
         return result;
    }
    public static void main(String[] args){
        int[] nums ={1,2,3};
        System.out.println();
        SubarraySumEqualsK solve=  new SubarraySumEqualsK();
        System.out.println(solve.subarraySum(nums,3));

    }
}
