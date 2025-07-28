public class MinimumWindowSubstring {
    public String minWindow(String s, String t) {
    //前置校验统计目标床t的字符需求
        if(s==null || t==null || s.length()<t.length() ){
            return "";
        }
        int[] need =new int[128];
        for (char c: t.toCharArray()){
            need[c]++;
        }
        int required=0;
        for(int cnt:need){
            if (cnt>0)required++;
        }

        int[] window = new int[128];
        int formed=0;
        int left =0 ,right=0;
        int minLen=Integer.MAX_VALUE;
        int minLeft=0;
       //右指针扩张
        while(right<s.length()){
            char c = s.charAt(right);
            window[c]++;
            if (window[c]==need[c]){
                formed++;
            }
            right++;
            while(formed==required){
                if(right-left<minLen){
                    minLen=right-left;
                    minLeft=left;
                }
                char d = s.charAt(left);
                window[d]--;
                if(window[d]<need[d]){
                    formed--;
                }
                left++;
            }
        }

    return (minLen==Integer.MAX_VALUE)?"": s.substring(minLeft,minLeft+minLen);
    }
}
