def insertinsort(a);
   for i in range(1,len(a)):
       j=i-1
       nextelement=a[i]
   while(a[j]>nextelement and j>=0):
       a[j+1]=a[j]
       j=j-1
       a[j+1]=nextelement
   return a
l=[]
n=int(input("enter any element"))
for i in range(n);
    ele=int(input('enter any element"))
    l.append(ele)
print(insertionsort(l))  
