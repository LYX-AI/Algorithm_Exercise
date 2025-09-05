package List;

import java.lang.reflect.Array;
import java.util.Arrays;

public class SquaresofaSortedArray {
    public int[] sortedSquares(int[] nums) {
        int[] result = new int[nums.length];
        int i =0;
        int j= nums.length-1;
        int k =nums.length-1;
        while(i<=j){
            if (nums[i]*nums[i]>nums[j]*nums[j]){
                result[k--]=nums[i]*nums[i];
                i++;
            }
            else{
                result[k--]=nums[j]*nums[j];
                j--;

            }

        }
        return result;
    }

    public static void main(String[] args ){
       int[] nums = {-4,-1,0,3,10};
       SquaresofaSortedArray solution = new SquaresofaSortedArray();
       System.out.println(Arrays.toString(solution.sortedSquares(nums)));
    }
}
