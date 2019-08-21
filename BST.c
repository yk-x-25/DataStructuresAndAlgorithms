#include<stdio.h>
#include<stdbool.h>
struct node
{
    int data;
    struct node* right;
    struct node* left;

};
struct node* root=NULL;
struct node* createnode(int data)
{
      struct node* temp=(struct node*)malloc(sizeof(struct node));
      temp->data=data;
      temp->right=temp->left=NULL;

    return temp;
}

struct node* insert_node(struct node* root,int data)
{
    if(root==NULL)
     return createnode(data);
    else if(root->data<data)
        root->right=insert_node(root->right,data);
    else
        root->left=insert_node(root->left,data);
    return root;
}

void print_inorder(struct node* root)
{
    if(root==NULL)
        return;
    //left nodes
    print_inorder(root->left);
    //middle node
    printf("%d\n",root->data);
    //right node
    print_inorder(root->right);
}


void delete_node(int data)
{

    if(root->data==data)
    {
        struct node*temp=root->right;
        while(temp->left!=NULL)
            temp=temp->left;

       temp->left=root->left;
       root=root->right;
    }

}
int main()
{

    int data;int n=5;
    ;
    while(n--){
    scanf("%d",&data);
    root=insert_node(root,data);
    }
//print_inorder(root);
printf("==========root%d==========\n",root->data);
delete_node(root->data);
printf("==========root%d==========\n",root->data);
print_inorder(root);
}
