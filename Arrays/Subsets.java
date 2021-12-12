class Subsets {
        
        public static void printBuffer(int[] buffer, int bufferIndex) {
            for( int i = 0 ; i < bufferIndex ; i++){
                System.out.print(buffer[i]);
            }
            System.out.println("\n");
        }

        public static void printSubsets(int[] givenNumber, int[] buffer , int startIndex, int bufferIndex){
            
                if((givenNumber == null) || (givenNumber.length == 0) ){
                    return;
                }

                if( startIndex > givenNumber.length){
                    return;
                }
                
                printBuffer(buffer, bufferIndex);

                for(int i = startIndex ; i < givenNumber.length ; i++){
                    buffer[bufferIndex] = givenNumber[i];
                    printSubsets(givenNumber, buffer, i+1, bufferIndex + 1);
                }
        }
        public static void main(String args[]){
            int[] givenNumber = {1,2,3};
            int[] buffer      = new int[givenNumber.length];
            int bufferIndex = 0;
            int startIndex  = 0;
            printSubsets(givenNumber,buffer,startIndex,bufferIndex);
        }
}
