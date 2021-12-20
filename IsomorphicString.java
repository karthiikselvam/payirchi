import java.util.HashMap;

public class IsomorphicString {
    public static boolean isIsomorphic(String s, String t) {
        HashMap<Character,Character> map1 = new HashMap<>();
        HashMap<Character,Character> map2 = new HashMap<>();
        for(int i = 0 ; i < s.length() ; i++){
             char char1 = s.charAt(i);
             char char2 = s.charAt(i);
             if(((map1.containsKey(char1) && map1.get(char1)!= char2)) || 
               ((map2.containsKey(char2) && map1.get(char2)!= char1))){
                 System.out.println(map1.get(char1)); 
                 return false;
             }   
               map1.put(char1, char2);
               map2.put(char2, char1);
            
        }
        return true;
    }

    public static void main(String [] args){
        String s = "foo";
        String t = "bar";
        boolean result = isIsomorphic(s,t);
        System.out.println(result);
    }


}