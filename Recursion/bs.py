import math
def binarySearch(start,end):
    mid = math.ceil((start+end)/2)
    res = input("is {} greater/small/equal? (g/s/=)".format(mid))
    if res == "=":
        return 
    if res == "g":
        return binarySearch(mid,end)
    else:
        return binarySearch(start,mid)

if __name__ == '__main__':
    binarySearch(1,2097151)
    