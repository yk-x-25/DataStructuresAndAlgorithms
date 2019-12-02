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
        
    
