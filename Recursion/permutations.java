import java.util.*;

class permutations{
	public static void printbuffer(int[] buffer){
		for( int i = 0 ;i < buffer.length; i++){
			System.out.print(buffer[i]);
		}
		System.out.println("");	
	}	
	
	
	public static void printpermutations(int[] arr, int[] buffer,boolean[] isInBuffer,int bufferIndex){
		if(bufferIndex == buffer.length){
			printbuffer(buffer);
			return;
		}
		for( int i =0; i < arr.length ; i++){
			if(!isInBuffer[i]){
				isInBuffer[i] = true;
				buffer[bufferIndex] = arr[i];
				printpermutations(arr,buffer,isInBuffer,bufferIndex+1);
				isInBuffer[i] = false;	
			}	
		}
	}
	public static void main(String [] args){
		int[] arr = {1,2,3};
		int[] buffer = new int[3];
		int bufferIndex= 0;
		boolean[] isInBuffer = new boolean[3];
		printpermutations(arr,buffer,isInBuffer,bufferIndex);
	}
}
