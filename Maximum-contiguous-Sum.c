#include<stdio.h>
#include<limits.h>
int return_max(int num1,int num2)
{

    return num1>num2?num1:num2;
}
int main()
{
    int size,ind;
    scanf("%d",&size);

    int arr[size];
    //O(n) extra space for visualizing dynamic approach or else it can be even done in O(1)
    int temp_arr[size];
    for(ind=0;ind<size;ind++)
        scanf("%d",&arr[ind]);
    int max=arr[0];
    temp_arr[0]=arr[0];
    for(ind=1;ind<size;ind++)
    {
        temp_arr[ind]=arr[ind]=return_max(arr[ind],arr[ind]+arr[ind-1]);
        if(max<arr[ind])
            max=arr[ind];


    }
    //print the Visualized white board array
for(ind=0;ind<size;ind++)
     printf("%d ",temp_arr[ind]);

 printf("\n Maximum sum is %d ",max);

}
