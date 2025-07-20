import java.util.HashSet;
import java.util.Set;
import java.lang.Math;
public class LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> result_set= new HashSet<>();
        int left=0;
        int result=0;
        for(int right=0;right<s.length();right++){
            while (result_set.contains(s.charAt(right))){
                result_set.remove(s.charAt(left));
                left+=1;
            }
            result_set.add(s.charAt(right));
            result=Math.max(result,right-left+1);
        }
        return result;
    }

}
