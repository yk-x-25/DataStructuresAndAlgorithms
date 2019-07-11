#include<stdio.h>
#include<stdbool.h>

int visited[5][5]={0};
int arr[5][5]={
{1,0,0,0,0},
{1,0,1,1,1},
{1,1,1,0,1},
{1,1,0,0,1},
{1,1,1,1,1}};

bool right(int row,int col)
{
 if(arr[row][col+1]==1&&col!=4)
    return true;
else
    return false;

}

bool bottom(int row,int col)
{
if(arr[row+1][col]==1&&row!=4)
    return true;
else
    return false;

}

bool left(int row,int col)
{

    if(arr[row][col-1]==1&&col!=0)
    return true;
else
    return false;

}

bool up(int row,int col)
{
if(row!=0&&arr[row-1][col]==1)
    return true;
else
    return false;

}

bool findpath(int row,int col)
{visited[row][col]=1;
    printf("%d %d\n",row,col);
    if(row==4&&col==4)
        return true;

if(right(row,col)&&visited[row][col+1]!=1)
  findpath(row,col+1);

else if(bottom(row,col)&&visited[row+1][col]!=1)
  findpath(row+1,col);


else if(left(row,col)&&visited[row][col-1]!=1)
  findpath(row,col-1);


else if(up(row,col)&&visited[row-1][col]!=1)
  findpath(row-1,col);


else
   return false;


}
int main()
{int i,j;

if(findpath(0,0))
 printf("exists\n");
else
    printf("no\n");
    for(i=0;i<5;i++,printf("\n"))
        for(j=0;j<5;j++)
printf("%d",visited[i][j]);
}
