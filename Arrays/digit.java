import java.util.Collections;
import java.util.HashMap;
import java.util.Map.Entry;

public class digit{
    
    public static void solution(int[] a) {
    HashMap<Character,Integer> hashtable = new HashMap<>();
    for( int num : a){
        String number = String.valueOf(num);
        char[] digits   = number.toCharArray();
        
        for(char digit : digits){
            int count = 1;
            if(hashtable.containsKey(digit)){
                count = hashtable.get(digit);
                count++;
                
            }
            hashtable.put(digit,count);
        }
        
    }
    int maxValueInMap=(Collections.max(hashtable.values()));  // This will return max value in the HashMap
        for (Entry<Character, Integer> entry : hashtable.entrySet()) {  // Iterate through HashMap
            if (entry.getValue()==maxValueInMap) {
                System.out.println(entry.getKey());     // Print the key with max value
            }
        }
    

    
}
    public static void main (String[] args){
        int[] number = {25, 2, 3, 57, 38, 41};
        solution(number);

    }
}