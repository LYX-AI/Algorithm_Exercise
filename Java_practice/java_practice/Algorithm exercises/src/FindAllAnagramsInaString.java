import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FindAllAnagramsInaString {
    public List<Integer> findAnagrams(String s, String p) {
            int m=s.length();
            int n=p.length();
            List<Integer> result=new ArrayList<>();
            char[] chars_p=p.toCharArray();
            Arrays.sort(chars_p);
            String sorted_p=new String(chars_p);
            for(int i=0;i<=m-n;i++){
                String sub_s=s.substring(i,i+n);
                char[] chars_s=sub_s.toCharArray();
                Arrays.sort(chars_s);
                String sorted_s=new String(chars_s);
                if(sorted_s.equals(sorted_p)){
                    result.add(i);
                }
            }
            return result;
    }
    public static void main(String[] args){
        FindAllAnagramsInaString solver=new FindAllAnagramsInaString();
        String s = "cbaebabacd";
        String p = "abc";
        List<Integer> result= solver.findAnagrams(s,p);
        System.out.println(result);
    }
}
