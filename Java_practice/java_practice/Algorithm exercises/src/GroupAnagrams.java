import java.util.*;

public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> temp=new HashMap<>();
        for(String word:strs){
            char[]  charArray = word.toCharArray();
            Arrays.sort( charArray);
            String key= new String(charArray);
            if (!temp.containsKey(key)){
                temp.put(key,new ArrayList<>());
            }
            temp.get(key).add(word);
        }
        Collection<List<String>> value=temp.values();
        List<List<String>> result=new ArrayList<>(value);
        return result;

    }

    public static void main(String[] args){
        GroupAnagrams ga= new GroupAnagrams();
        String[] strs={"eat", "tea", "tan", "ate", "nat", "bat"};
        List<List<String>> result =ga.groupAnagrams(strs);
        System.out.println(result);
    }
}
