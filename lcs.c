#include<stdio.h>
#include<limits.h>


int main()
{   int size,max=INT_MIN,contd=1;
while(contd){
   scanf("%d",&size);
   int *arr=(int*)malloc(sizeof(int)*size);

    int q_i=0,i,j,ct=1;
    for(i=0;i<size;i++)
      {
        scanf("%d",&arr[i]);
        if(arr[i]>max)
            max=arr[i];

      }
      int* hash_table=(int*)calloc(sizeof(int),max);

    int* visited=(int*)calloc(sizeof(int),max+1);
    for(i=0;i<size;i++)
        hash_table[arr[i]]=1;

    max=INT_MIN;int ind=1;
    for(i=0;i<size;i++)
    {
        if(visited[arr[i]]==0&&hash_table[arr[i]-1]==1)
        {
           while(hash_table[arr[i]-ind]==1)
            {
                visited[arr[i]-ind]=1;
                ind++;
                ct++;}
            }
        ind=1;
      while(hash_table[arr[i]+ind]==1&&visited[arr[i]+ind]==0)
        {
              visited[arr[i]+ind]=1;
              ind++;
              ct++;
        }
        if(max<ct)
            max=ct;
        ct=ind=1;
    }


printf("max consecutive %d",max);
printf("Wanna contd?(1/0)");
scanf("%d",&contd);

}return 0;
}
