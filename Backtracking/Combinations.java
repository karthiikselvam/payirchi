public class Combinations{

    public static void printCombosHelper(int[] numbers, int[] buffer , int startIndex , int bufferIndex){

        if( bufferIndex == buffer.length){
            for(int num : buffer){
                System.out.print(num);
            }
            System.out.println();
            return;
        }

        if(startIndex == numbers.length){
            return;
        }

        for(int i = startIndex ; i < numbers.length; i++){
            buffer[bufferIndex] = numbers[i];
            printCombosHelper(numbers, buffer, i+1, bufferIndex + 1);
        }
    }

    public static void main( String args []){
        int[] numbers = {1,2,3};
        int[] buffer  = new int[2];

        int startIndex = 0;
        int bufferIndex = 0;

        printCombosHelper(numbers, buffer , startIndex, bufferIndex );
    }

}