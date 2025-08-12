import java.util.Arrays;

public class RotateArray {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        if (n==0){
            return;
        }
        k %=n;
        for (int t=0;t<k;t++){
            int The_Last=nums[n-1];
            for (int i=n-1;i>0;i--){
                nums[i]=nums[i-1];
            }
            nums[0]=The_Last;
        }

    }
    public static void main(String[] args){
        RotateArray solution= new RotateArray();
        int[] nums = {1,2,3,4,5,6,7};
        int k =3;
        solution.rotate(nums,k);
        System.out.println(Arrays.toString(nums));

    }
}
