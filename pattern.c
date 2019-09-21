/*
print the pattern
for input=4
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111

*/
#include<stdio.h>
int i;
int print_bin(int num)
{if(num<=1)
  return num;

return(num%2)+10*print_bin(num/2);;
}

int main()
{int num=4,stop=2;
for(i=1;i<num;i++)
    stop*=2;
for(i=0;i<stop;i++,printf("\n"))
  printf("%.*d",num,print_bin(i));

}
