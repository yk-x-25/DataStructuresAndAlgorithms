'''
HEAP DATA STRUCTURE
- Don't confuse heap as a tree. Heap is basically represented as an array and hence linear

arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

Corresponding Complete Binary Tree is:
                 1
              /     \
            3         5
         /    \     /  \
        4      6   13  10
       / \    / \
      9   8  15 17

Leaf Node :
A node w/o children

Full Binary tree:
All the nodes except the leaves have 2 children

Complete Binary tree:
All the nodes except the last level is full. All the leaves are leftmost.

Max Heap:
Parent is always greater than either of the children

MinHeap :
Parent is always Lesser than either of the children

Last Non Leaf Node:
index : n//2-1

#######

Time Complexity :

Building Heap:
- O(NLogN)
Deletion (root) :
- O(LogN)
Insertion
- O(LogN)
Peak/min Peak Finding
- O(1)
Searching 
- O(N)

'''

# This function will take Log(N) time
def heapify(arr,i):
    leftChild = 2*i+1
    rightChild = 2*i+2
    largestIndex =i 
    
    if leftChild<len(arr) and arr[i] < arr[leftChild]:
        largestIndex = leftChild
    if rightChild<len(arr) and  arr[largestIndex] < arr[rightChild]:
        largestIndex = rightChild
    if i!=largestIndex:
        arr[i],arr[largestIndex] =arr[largestIndex],arr[i]
        # recursively heapify subtree
        heapify(arr,largestIndex)

def buildHeap(arr):
    n = len(arr)
    # We just need to heapify from the last non leaf node until root
    startIdx = n // 2 - 1; 
 
    for i in range(startIdx, -1, -1): 
        heapify(arr,  i); 


def heapifyBottomUp(arr,index):
    parent =(index-1)//2
    if parent >=0 and arr[parent]  < arr[index]:
        arr[parent] , arr[index] =  arr[index], arr[parent]
        heapifyBottomUp(arr,parent)

'''
Insertion Into Heap:

Algorithm:
- We'd be inserting to the left most node. 
- Just have to check the inserted node with the parent (can be < or > depending on type)
   and swap with parent if it satisfies
- Continue step 2 until root (this is typically a heapify bottom-up)
'''
def insertIntoHeap(val,arr):
    arr.append(val)
    heapifyBottomUp(arr,len(arr)-1)

'''
Deleting Root:
We usually delete the root element.
Even if we are to delete some generic element , it would take the below complexity
Time Complexity : O(N) for finding the index + O(logN) for heapify  =  O(N)

Algorithm:
- swap the last node with the root
- shrink the array / pop the last element (that will be the element to be deleted)
- Heapify from top
'''

def deleteElem(arr):
    idx= 0
    arr[idx],arr[-1] = arr[-1],arr[idx]
    arr.pop(-1)
    heapify(arr,idx)

if __name__ == '__main__':
    arr = [83, 68, 75, 58, 73, 8, 43, 29, 58, 34, 1, 2, 2, 5, 11, 28, 24]
    buildHeap(arr)
    print("Before insetion & del {}".format(arr))

    deleteElem(arr)
    deleteElem(arr)
    insertIntoHeap(5,arr)

    print("after insetion & del {}".format(arr))
