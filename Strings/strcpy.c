char* stringcopy(char* source , char* destination){
	char* strresult = destination ;
	if(source != NULL) && (destination != NULL){
		while( source != NULL){
			*destination = *source;
			*destination++;
			*source++;
		}
		*destination = NULL
	}
	return strresult;
}
