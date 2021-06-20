char* strcat(char* destination , char* source){
	char* strresult = destination;
	if(*destination != NULL){
		while(*destination != NULL){
			destination++;
		}	
		while(*source != Null){
			*destination = *source;
			*destination++;
			*source++;
		}
		*destination = NULL;
	}
	return strresul;
}
