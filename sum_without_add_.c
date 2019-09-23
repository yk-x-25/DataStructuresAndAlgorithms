#include<stdio.h>
int main()
{
int a=560982,b=2132,carry;

while(b!=0)
{
    carry=a&b;
    a=a^b;
    b=carry<<1;

}
printf("sum=%d",a);
}
