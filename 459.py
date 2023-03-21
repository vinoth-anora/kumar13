l=[1,23,4,5,6,7]
for i in range(0,len(l)):
   for j in range(0,len(l)):
      if l[i]<l[j]:
         l[i],l[j]=l[j],l[i]
print(l)

