import java.util.Arrays;

public class ProductofArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        Arrays.fill(result,1);
        int prfix = 1;
        for (int i=0;i<nums.length;i++){
            result[i] = prfix;
            prfix *= nums[i];
        }
        int suffix = 1;
        for (int i = nums.length-1;i>-1;i--){
            result[i]*=suffix;
            suffix *= nums[i];
        }
        return result;
    }
    public static void main(String[] args){
        ProductofArrayExceptSelf solution= new ProductofArrayExceptSelf();
       int[] nums ={1,2,3,4};
       System.out.print(Arrays.toString(solution.productExceptSelf(nums)));
    }
}
