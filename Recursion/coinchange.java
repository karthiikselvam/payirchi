import java.util.*;

class coinchange{
	public static void print(Stack<Integer> buffer){
		for(Integer ele : buffer){
			System.out.print(ele);
		}
		System.out.println("");
	}
	public static void coinchangesum(int[] coins, int target, int startIndex,Stack<Integer> buffer,int sum){
		if(sum  > target){
			return;
		}	
		if(sum == target){
		     print(buffer);
		     return;
		}
		for(int i = 0; i < coins.length; i++){
			buffer.push(coins[i]);
			coinchangesum(coins,target,i,buffer,sum+coins[i]);
			buffer.pop();
		}
	}
	public static void main(String [] args){
		int[] coins = {1,2,5};
		int target  = 5;
		int startIndex = 0;
		Stack<Integer> buffer = new Stack<>();
		coinchangesum(coins,target,startIndex,buffer,0);
	}
}
