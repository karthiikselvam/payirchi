class moveevennumbers{

	public static int getIndex(int arr[]){
		int i = arr.length - 1;
		while(i >=0 && arr[i] == -1){
			i--;
		}	
		return i;
	}	


	public static void main( String [] args){

		int arr[] = {1,2,5,6,8,-1,-1,-1}; 
		int lastIndex = getIndex(arr);
		int last  = arr.length - 1;	
		while( lastIndex >= 0){
			if( arr[lastIndex] % 2 == 0){
				arr[last] = arr[lastIndex];	
				last--;
			}
				arr[last] = arr[lastIndex];
				lastIndex--;
				last--;
		}
		int i =0 ;
		for( i = 0 ; i < arr.length ; i++){
			System.out.print(arr[i]);
		}
	}

}
