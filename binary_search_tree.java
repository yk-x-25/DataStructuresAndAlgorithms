public class bintree
{
	public static void main(String[] args) {
		tree btree=new tree();
		tree root=null;
		root=btree.addnodes(50,root);
		btree.addnodes(40,root);
		btree.addnodes(90,root);
		btree.addnodes(100,root);
		btree.addnodes(10,root);
		btree.addnodes(8,root);
		btree.addnodes(12,root);
	btree.printtree(root);
}
}
class tree
{
	tree left,right;
	int data;
	tree(){}
	tree(int n)
	{
		left=null;right=null;data=n;
	}
	public tree createnode(int data,tree root)
	{  root=new tree(data);
		return root;
	}
	public tree addnodes(int data,tree node)
	{
		if(node==null)
			return createnode(data,node);
		else if(data>node.data)
			node.right=addnodes(data,node.right);
		else
		   node.left=addnodes(data,node.left);
		return node;			
	}
	public void printtree(tree root)
	{
		if(root==null)
			return;
		printtree(root.left);
		System.out.println(root.data);
		printtree(root.right);
	}
}







