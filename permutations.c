#include<stdio.h>
#include<string.h>
void swap(char* s,int i,int j)
{   char temp;
    temp=s[i];
    s[i]=s[j];
    s[j]=temp;
}
char word[320][100];
void fun_permute(char* str,int start,int end)
{int i;
static int ct=0,limit,index;
if(start==end)
 printf("%d %s\n",++ct,str);

     else
     {

         for(i=start;i<end;i++)
         {
              swap(str,start,i);
              fun_permute(str,start+1,end);
               swap(str,start,i);
         }
     }
}
int main()
 {
char s[10];
printf("Enter the string with distinct characters(max 10)");
scanf("%s",s);
int len=strlen(s);
fun_permute(s,0,len);

 }

/*

d o g
d g o
o d g
o g d
g o d
g d o
*/


/*

l o s t--o l s t--s o l t.......
l o t s--o l t s--s o t l.......
l s o t--o s l t--s l o t.......
l s t o--o s t l--s l t o.......
l t s o--o t l s--s t o l .......
l t o s--o t s l--s t l o  .......
*/
/*
f r i d a y.......
f r i d y a.......
f r i a d y.......
f r i a y d.......
f r i y d a.......
f r i y a d.......


*/
