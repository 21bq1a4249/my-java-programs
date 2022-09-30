def Binarysearch(l,low,high,key):
     while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=mid-1
        else:
            low=mid+1
     return -1
l=[1,2,3,4,5,6,9]
low=0
high=len(l)
key=int(input("enter any value"))
result=Binarysearch(l,low,len(l)-1,key)
if result==-1:
    print("element not found")
else:
   print("element found at",result)
