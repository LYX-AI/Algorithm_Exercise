import java.lang.Math;
public class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int n = height.length;
        int left =0;
        int right=n-1;
        int max_area=0;

        while (left<=right){
            int w=right-left;
            int h=Math.min(height[right],height[left]);
            int area=w*h;
            max_area=Math.max(area,max_area);

            if (height[left]< height[right]){
                left=left+1;
            }
            else {
                right=right-1;
            }
        }
        return max_area;
    }

    public static void main(String[] args){
        ContainerWithMostWater obj=new ContainerWithMostWater();
        System.out.println();
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7}; // 示例输入
        int result = obj.maxArea(height);
        System.out.println("最大装水量是: " + result); // 应输出 49
    }
}
