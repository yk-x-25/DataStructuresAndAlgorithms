'''
Arrays are sequential ds
they are allocated with contiguous memory blocks
you can simply use the implementation below as 
* Stack 
* Queue

'''
# this is how we declare in python
arr=[]
arr=    [1,2,3,4,5]
# index  0 1 2 3 4 

'''
# STACK 
* PUSH
visual   idx              

| 7 |  <- 3  (newly pushed)
-----
| 8 |  <- 2
-----
| 6 |  <- 1
----- 
| 5 |  <- 0
-----

* POP
| 8 |  <- 2
-----
| 6 |  <- 1
----- 
| 5 |  <- 0
-----

| 7 |  <- 3  (popped elem)
-----

Stack follows LIFO.
Last In First Out -  Think of plates stacked on top of each other . You'd always pick the topmost plate

'''

n = int(input())
plates = []
# push 
for _ in range(n):
    plate = int(input())
    print("Plate {} is pushed".format(plate))
    plates.append(plate)
# pop 
for _ in range(n):
    removedPlate = plates.pop(-1)
    print("Plate {} is popped remaining plate {}".format(removedPlate,plates))






