# #Linked List
Whenever I hear the word Linked List, The first thing that buzz off is the fact that it contains data and the next node's value. But, Why do we Actually have a Linked List? Where do we use it? The answer is simple!.==>NOWHERE. Linked list is to confuse you in the coding Interview!.
Anyways, Here's what you need 
```python
class linkedlist:
    def __init__(self,val):    
        self.next=None
        self.val=val
```
* ### The Deep Dive into the Linked List
  Well,Let's take a Train, Each coaches are linked to one another. Even if One of the coaches fall apart, You lose the remaining coaches after the coach that is disconnected! 
  Wait,What? Heard the same somewhere else? Yes,it is BLOCKCHAIN.
* ### Alright, Let's insert into linked list
    All we want is ``` | 1 --> 2 --> 3 --> 4 | ```. But, how do we make it? 
    The simplest solution is 
    * Create a head node assign it as None/Null
    * If head is none, there's no elements present in the linked list. So, we make the current element as the head element
    * After adding the head element, the next element that stacks up will have to be connected to the previous element.
    ```python
    temp_head=None
    head=None
    def insert(value):
      if not head:
        #first elemnt to be added
        head=linkedlist(val)
        temp_head=head
      else:
        temp_head.next=linkedlist(val)
        temp_head=temp_head.next
     ```
        
# #Graphs
Wonder How Facebook recommends your friends' friend? Yes, FB uses graphs. **"Every ALGORITHM is totally created by observations from environment"**. Algorithm Recommending friends is built on human nature to introduce new people to their friends' or family.
Consider Each Human as a node, Each of him friends hold hands with him so that all of them are connected to him/her. 

Analogous to graphs it is Vertices and Edge. Where the **Vertex(Singular)** is the human and the hands that are connecting each of 
the human's friends are the **Edges**.

Let's get started with making a graph. I've a weird way and not-to-do way of coding style. That's basically how you start to learn things.

First of all, We need to create a node. Let's say I have a data field that holds my data and Also, I need a List of links that are connected to the node. 

**NOTE:** We used a single link field in the lined list as we know each node can only be connected to the next node.
```python
class node:
    def __init__(self,data):
        self.data=data
        self.link=[]
```
And Let's add The nodes to the graph .

**Please do not follow the same code as you step higher from beginner The code below is completely meant for easier understanding**

```python
head=None
def create_graph(data,parents):
    global head
    created_node=node(data)
    #if it is the first node of the graph
    if parents is None:
        head=created_node
        return head    
    # append the created node to each parent (creating an edge) to form a link between 'em.
    for every_parent in parents:
      every_parent.link.append(created_node)
    return created_node 
```
And finally the main function goes here.
```python
if __name__ == '__main__':
    first=create_graph(1,None)
    second=create_graph(2,[first])
    third=create_graph(3,[first])
    fourth=create_graph(4,[second,third])
    first.link.append(fourth)
    fifth=create_graph(5,[fourth])
```
**Woah! We've completed step 0.000001 of creating a brand new FB**
* # Travesals
  * Breadth First Search
  * Depth First Search
    * **BFS**
    
    **Unlike other youtube tutorials,I've focussed much less on stack,Queues and Arrays/ArrayList because they are all included in these major Ds that are used. **
   
    We make use of Queue here. 
    
    Let's take a situation here . You and 4 of your friends are about to buy a ticket for a movie. Instead of all 5 of you standing in the line buying each one ,a ticket,you yourself can go and buy 5 tickets.What we observe here is that all the 4 of your friends can be refernced by a single entity(i.e you). Let's say a 6 th person who happens to be your friend's friend wants a ticket but she is too lazy to stand in the line neither she wishes to break the line. Instead, She finds your friend and tells her that she wants a ticket.So,your friend tells you to buy an extra ticket.
    
    What we infer here is that
    > Any node can be referenced by any other node given that it has a indirect link.
    ```python
    def bfs():
        queue=[]
        queue.append(head)
        visited=set()

        while queue:
            temp=queue.pop(0)

            queue.extend(temp.link)
            if temp not in visited:
                print([i.data for i in queue],end="<--->")
                visited.add(temp)
                print(temp.data) 

```

# N QUEENS

```
________________________
|Q_|__|__|__|__|__|__|__|
|__|__|__|__|Q_|__|__|__|
|__|__|__|__|__|__|__|Q_|
|__|__|__|__|__|Q_|__|__|
|__|__|Q_|__|__|__|__|__|
|__|__|__|__|__|__|Q_|__|
|__|Q_|__|__|__|__|__|__|
|__|__|__|Q_|__|__|__|__|
```
