import java.util.*;
class fibonaccimemo{

	public static int fibonacci(int n , Map<Integer,Integer>memo){
		if(n == 1 || n == 2){
			return 1;
		}
		if(memo.containsKey(n))	{
			return memo.get(n);
		}
		int result = fibonacci(n-1,memo) + fibonacci(n-2,memo);
		memo.put(n,result);
		return result;
	}


	public static void main(String [] args){
		int n = 5;
		Map<Integer,Integer> memo = new HashMap<Integer,Integer>();
		int result = fibonacci(n,memo);
		System.out.println(result);		

	}

}
