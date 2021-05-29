import java.util.*;
class combinations{
	public static void printBuffer(int[] buffer){
		for( int i =0 ; i < buffer.length; i++){
			System.out.print(buffer[i]);
		}
		System.out.println("");
	}

	public static void printCombos(int[] arr , int[] buffer , int bufferIndex,int startIndex){
		if(bufferIndex == buffer.length){
			printBuffer(buffer);
			return	;
		}
		if(startIndex == arr.length){
			return;
		}
		for(int i = startIndex; i < arr.length; i++){
			buffer[bufferIndex] = arr[i];
			printCombos(arr,buffer,bufferIndex + 1, i+1);
		}
	}
	public static void main(String [] args){
		int[] arr = {1,2,3,4};
		int[] buffer = new int[3];
		int bufferIndex = 0;
		int startIndex = 0;
		printCombos(arr, buffer,bufferIndex,startIndex);
	}
}
