int strlen(char* source){
	int length = 0;
	if(*source != NULL){
	while(*source != NULL){ 
		length++;
		source++;
	}
	return length;
}
