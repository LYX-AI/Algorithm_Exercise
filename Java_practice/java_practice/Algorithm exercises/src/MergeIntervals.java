import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.lang.Math;

public class MergeIntervals {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->Integer.compare(a[0],b[0]));
        List<int[]> merged= new ArrayList<>();
        for (int[]intercal:intervals){
            if(merged.isEmpty()|| merged.get(merged.size()-1)[1]<intercal[0]){
                merged.add(new int[]{intercal[0],intercal[1]});
            }else{
                int [] last=merged.get(merged.size()-1);
                last[1]=Math.max(last[1],intercal[1]);
            }
        }
        return merged.toArray(new int[merged.size()][]);
    }

}
