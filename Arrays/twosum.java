import java.util.Arrays;
import java.util.*;
class twosum {
        public static void main(String [] args){
        int[] nums = {2,7,11,15};
        int target =    9;
        Arrays.sort(nums);
        int startptr = 0;
        int endptr   = nums.length - 1;
        int[] res    = new int[2];
        while (startptr < endptr){
            
            if((nums[startptr] + nums[endptr]) < target){
                startptr++;
            }else if((nums[startptr] + nums[endptr]) > target){
                endptr--;
            }else{
                res[0]  = startptr;
                res[1]  = endptr;
                break;
            }
            
            
        }
        for( int j = 0 ; j < res.length; j++){
                System.out.println(res[j]);
        }
    }
}