#include<stdio.h>

unsigned short field[15];
unsigned short checksum() {
  int i, sum = 0;
  printf("enter the IP header information in 16 bit words\n");
  for (i = 0; i < 9; i++) {
    printf("field:%d\n", i + 1);
    scanf("%x", & field[i]);
    sum = sum + (unsigned short) field[i];
    while (sum >> 16) {
      sum = (sum & 0xFFFF) + (sum >> 16);
    }
  }
  sum = ~sum;
  return (unsigned short) sum;
}

int main() {
  unsigned short result1, result2;
  result1 = checksum();
  printf("sender checksum %x\n", result1);
  result2 = checksum();
  printf("receiver checksum %x\n", result2);
  if (result1 == result2) {
    printf("no error\n");
  } else {
    printf("error\n");
  }
}
