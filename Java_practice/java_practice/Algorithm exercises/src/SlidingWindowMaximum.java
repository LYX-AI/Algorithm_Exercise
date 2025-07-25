import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class SlidingWindowMaximum {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(nums==null||k<=0){
            return new int[0];
        }
        int n =nums.length;
        int[] reslut=new int[n-k+1];
        Deque<Integer>deque=new ArrayDeque<>();
        int ri=0;
        for(int i =0;i<n;i++){
            if(!deque.isEmpty()&&deque.peekFirst()<i-k+1){
                deque.pollFirst();
            }
            while (!deque.isEmpty()&&nums[deque.peekLast()]<=nums[i]){
                deque.pollLast();
            }
            deque.addLast(i);
            if(i>=k-1){
                reslut[ri++]=nums[deque.peekFirst()];
            }
        }
        return reslut;
    }
}
