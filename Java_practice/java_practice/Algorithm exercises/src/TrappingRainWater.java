public class TrappingRainWater {
    public int trap(int[] height) {
        if(height==null||height.length==0){
            return 0;
        }
        int n = height.length;
        int left=0;
        int rigt=n-1;
        int water=0;
        int max_left=0;
        int max_right=0;
        while(left<rigt){
            if (height[left]<height[rigt]){
                if(height[left]>=max_left){
                    max_left=height[left];
                }
                else {
                    water+=max_left-height[left];
                }
                left+=1;
            }
            else {
                if(height[rigt]>=max_right){
                    max_right=height[rigt];
                }
                else {
                    water+=max_right-height[rigt];
                }
                rigt-=1;
            }
        }
        return water;
    }

}
